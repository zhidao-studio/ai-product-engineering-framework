#!/usr/bin/env python3
"""检查验证证据清单的结构与结论约束。

该脚本不执行清单中的命令，也不判断证据真实性、产品正确性或用户满意度。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


RISK_LEVELS = {"low", "medium", "high", "critical"}
LAYERS = {"static", "runtime", "user", "release"}
EVIDENCE_STATUSES = {
    "passed",
    "failed",
    "blocked",
    "not_executed",
    "not_applicable",
}
OVERALL_RESULTS = {
    "passed",
    "conditional_pass",
    "failed",
    "blocked",
    "not_executed",
}
FORMAL_RESULTS = {"passed", "failed", "blocked", "not_executed"}
REQUIRED_TOP_STRINGS = (
    "manifest_version",
    "task_id",
    "repository",
    "baseline_commit",
    "risk_level",
    "overall_result",
    "formal_business_validation",
)
REQUIRED_EVIDENCE_FIELDS = (
    "id",
    "layer",
    "assertion",
    "required",
    "status",
    "executed",
    "step",
    "exit_code",
    "result_summary",
    "evidence_path",
    "actor",
    "executed_at",
)


class EvidenceManifestError(ValueError):
    """证据清单无效。"""


def load_manifest(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvidenceManifestError(f"无法读取证据清单: {exc}") from exc
    if not isinstance(data, dict):
        raise EvidenceManifestError("证据清单根节点必须是对象")
    return data


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_manifest(data: dict) -> list[str]:
    problems: list[str] = []

    for key in REQUIRED_TOP_STRINGS:
        if not _nonempty_string(data.get(key)):
            problems.append(f"缺少有效字段: {key}")

    if data.get("risk_level") not in RISK_LEVELS:
        problems.append(f"risk_level 无效: {data.get('risk_level')}")
    if data.get("overall_result") not in OVERALL_RESULTS:
        problems.append(f"overall_result 无效: {data.get('overall_result')}")
    if data.get("formal_business_validation") not in FORMAL_RESULTS:
        problems.append(
            "formal_business_validation 无效: "
            f"{data.get('formal_business_validation')}"
        )

    required_layers = data.get("required_layers")
    if not isinstance(required_layers, list) or not all(
        isinstance(item, str) and item in LAYERS for item in required_layers
    ):
        problems.append("required_layers 必须是允许的证据层数组")
        required_layers = []
    elif len(required_layers) != len(set(required_layers)):
        problems.append("required_layers 不能重复")

    evidence = data.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        problems.append("evidence 必须是非空数组")
        return problems

    seen_ids: set[str] = set()
    valid_items: list[dict] = []
    for index, item in enumerate(evidence):
        prefix = f"evidence[{index}]"
        if not isinstance(item, dict):
            problems.append(f"{prefix} 必须是对象")
            continue
        missing = [key for key in REQUIRED_EVIDENCE_FIELDS if key not in item]
        if missing:
            problems.append(f"{prefix} 缺少字段: {', '.join(missing)}")
            continue

        evidence_id = item["id"]
        if not _nonempty_string(evidence_id):
            problems.append(f"{prefix}.id 必须是非空字符串")
        elif evidence_id in seen_ids:
            problems.append(f"证据编号重复: {evidence_id}")
        else:
            seen_ids.add(evidence_id)

        if item["layer"] not in LAYERS:
            problems.append(f"{prefix}.layer 无效: {item['layer']}")
        if not _nonempty_string(item["assertion"]):
            problems.append(f"{prefix}.assertion 不能为空")
        if not isinstance(item["required"], bool):
            problems.append(f"{prefix}.required 必须是布尔值")
        if item["status"] not in EVIDENCE_STATUSES:
            problems.append(f"{prefix}.status 无效: {item['status']}")
        if not isinstance(item["executed"], bool):
            problems.append(f"{prefix}.executed 必须是布尔值")

        if item["status"] in {"passed", "failed"} and item["executed"] is not True:
            problems.append(f"{prefix} 标记 {item['status']} 时 executed 必须为 true")

        if item["executed"] is True:
            for key in ("step", "result_summary", "evidence_path", "actor", "executed_at"):
                if not _nonempty_string(item[key]):
                    problems.append(f"{prefix}.{key} 在已执行时不能为空")
            exit_code = item["exit_code"]
            if exit_code is not None and (
                isinstance(exit_code, bool) or not isinstance(exit_code, int)
            ):
                problems.append(f"{prefix}.exit_code 必须是整数或 null")

        valid_items.append(item)

    required_items = [
        item for item in valid_items if item.get("required") is True
    ]
    overall = data.get("overall_result")
    formal = data.get("formal_business_validation")

    if overall == "passed":
        unfinished = [
            item.get("id", "?")
            for item in required_items
            if item.get("status") != "passed"
        ]
        if unfinished:
            problems.append(
                "overall_result=passed 但必需证据未通过: " + ", ".join(unfinished)
            )

    if overall == "failed" and not any(
        item.get("required") is True and item.get("status") == "failed"
        for item in valid_items
    ):
        problems.append("overall_result=failed 但没有必需证据标记为 failed")

    if formal == "passed":
        if overall != "passed":
            problems.append(
                "formal_business_validation=passed 要求 overall_result=passed"
            )
        for layer in ("static", "runtime", "user"):
            if not any(
                item.get("layer") == layer
                and item.get("required") is True
                and item.get("status") == "passed"
                for item in valid_items
            ):
                problems.append(f"正式业务通过缺少 {layer} 层必需通过证据")

    for layer in required_layers:
        if not any(
            item.get("layer") == layer and item.get("required") is True
            for item in valid_items
        ):
            problems.append(f"required_layers 声明 {layer}，但没有该层必需证据")

    return problems


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="检查验证证据清单结构和结论约束")
    parser.add_argument("--manifest", required=True, type=Path, help="证据清单 JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = load_manifest(args.manifest)
    except EvidenceManifestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    problems = validate_manifest(data)
    print(f"任务: {data.get('task_id', 'unknown')}")
    print(f"证据项: {len(data.get('evidence', [])) if isinstance(data.get('evidence'), list) else 0}")
    print(f"总体结果: {data.get('overall_result', 'unknown')}")
    if problems:
        print("证据清单检查不通过:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("证据清单检查通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
