#!/usr/bin/env python3
"""根据候选任务控制清单检查 Git 修改路径。

该脚本只判断确定性的路径、依赖文件和高风险授权，不判断代码语义、
产品正确性、外部系统副作用或用户体验。
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable


RISK_LEVELS = {"low", "medium", "high", "critical"}
REQUIRED_LIST_FIELDS = (
    "allowed_paths",
    "forbidden_paths",
    "high_risk_paths",
    "approved_high_risk_paths",
    "dependency_files",
    "approved_dependency_files",
)


class ManifestError(ValueError):
    """任务控制清单无效。"""


def normalize_path(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized.lstrip("/")


def matches(path: str, pattern: str) -> bool:
    path = normalize_path(path)
    pattern = normalize_path(pattern)
    if not pattern:
        return False
    if pattern.endswith("/"):
        prefix = pattern.rstrip("/")
        return path == prefix or path.startswith(prefix + "/")
    if any(char in pattern for char in "*?["):
        if fnmatch.fnmatchcase(path, pattern):
            return True
        if pattern.startswith("**/"):
            return fnmatch.fnmatchcase(path, pattern[3:])
        return False
    return path == pattern


def matches_any(path: str, patterns: Iterable[str]) -> bool:
    return any(matches(path, pattern) for pattern in patterns)


def load_manifest(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ManifestError(f"无法读取任务控制清单: {exc}") from exc

    for key in ("manifest_version", "task_id", "risk_level"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ManifestError(f"缺少有效字段: {key}")
    if data["risk_level"] not in RISK_LEVELS:
        raise ManifestError(f"risk_level 无效: {data['risk_level']}")
    for key in REQUIRED_LIST_FIELDS:
        value = data.get(key)
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ManifestError(f"字段必须是字符串数组: {key}")
    if not data["allowed_paths"]:
        raise ManifestError("allowed_paths 不能为空")
    return data


def git_paths(repo: Path, mode: str, base: str | None, head: str) -> list[str]:
    def run(*args: str) -> list[str]:
        result = subprocess.run(
            ["git", "-C", str(repo), "-c", "core.quotePath=false", *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return [normalize_path(item) for item in result.stdout.splitlines() if item.strip()]

    try:
        if mode == "staged":
            paths = run("diff", "--cached", "--name-only")
        elif mode == "range":
            if not base:
                raise ManifestError("range 模式需要 --base 或清单 baseline_commit")
            paths = run("diff", "--name-only", base, head)
        else:
            paths = run("diff", "--name-only")
            paths += run("diff", "--cached", "--name-only")
            paths += run("ls-files", "--others", "--exclude-standard")
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or str(exc)
        raise ManifestError(f"Git 路径读取失败: {message}") from exc
    return sorted(set(paths))


def evaluate_paths(paths: Iterable[str], manifest: dict) -> list[str]:
    violations: list[str] = []
    for raw_path in sorted(set(paths)):
        path = normalize_path(raw_path)
        if matches_any(path, manifest["forbidden_paths"]):
            violations.append(f"禁止修改: {path}")
            continue
        if not matches_any(path, manifest["allowed_paths"]):
            violations.append(f"超出允许范围: {path}")
            continue
        if matches_any(path, manifest["high_risk_paths"]) and not matches_any(
            path, manifest["approved_high_risk_paths"]
        ):
            violations.append(f"高风险路径未授权: {path}")
        if matches_any(path, manifest["dependency_files"]) and not matches_any(
            path, manifest["approved_dependency_files"]
        ):
            violations.append(f"依赖文件未授权: {path}")
    return violations


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="检查任务修改路径是否符合控制清单")
    parser.add_argument("--manifest", required=True, type=Path, help="任务控制清单 JSON")
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Git 仓库路径")
    parser.add_argument("--mode", choices=("worktree", "staged", "range"), default="worktree")
    parser.add_argument("--base", help="range 模式基线，默认使用清单 baseline_commit")
    parser.add_argument("--head", default="HEAD", help="range 模式目标提交")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = load_manifest(args.manifest)
        base = args.base or manifest.get("baseline_commit")
        paths = git_paths(args.repo, args.mode, base, args.head)
        violations = evaluate_paths(paths, manifest)
    except ManifestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"任务: {manifest['task_id']}")
    print(f"风险: {manifest['risk_level']}")
    print(f"检查路径数: {len(paths)}")
    if violations:
        print("边界检查不通过:")
        for violation in violations:
            print(f"- {violation}")
        return 1
    print("边界检查通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
