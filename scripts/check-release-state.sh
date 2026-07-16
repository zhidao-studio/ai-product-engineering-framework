#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

fail() {
  printf 'ERROR: %s\n' "$1" >&2
  exit 1
}

require_file() {
  [[ -f "$1" ]] || fail "缺少文件: $1"
}

heading() {
  printf '\n==== %s ====\n' "$1"
}

require_file VERSION
require_file README.md
require_file AGENTS.md
require_file CHANGELOG.md
require_file 10_版本演进/Roadmap.md
require_file 12_框架项目Context/README.md

release="$(tr -d '[:space:]' < VERSION)"
[[ "$release" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || fail "VERSION格式错误: $release"
release_tag="v$release"

target_release="v0.2.0"
current_milestone="A / Context 可执行化"
youyu_release="v0.1.3"
formal_validation="not_started"
context_maturity="candidate"
database_maturity="candidate"
harness_b="not_started"

heading "稳定版本一致性"
grep -Fq "当前稳定版本：$release_tag" README.md || fail "README稳定版本不一致"
grep -Fq "## [$release] - 2026-07-16" CHANGELOG.md || fail "CHANGELOG缺少当前版本发布段"
grep -Fq "| $release_tag | 已完成 |" 10_版本演进/Roadmap.md || fail "Roadmap缺少当前版本历史行"
grep -Fq "stable_release: $release_tag" 12_框架项目Context/README.md || fail "Context稳定版本不一致"

heading "目标版本与里程碑一致性"
grep -Fq "目标开发版本：$target_release" README.md || fail "README目标版本不一致"
grep -Fq "target_release: $target_release" 12_框架项目Context/README.md || fail "Context目标版本不一致"
grep -Fq "current_milestone: $current_milestone" 12_框架项目Context/README.md || fail "Context当前里程碑不一致"
grep -Fq "当前里程碑：$current_milestone" README.md || fail "README当前里程碑不一致"
grep -Fq "### 里程碑 A：Context 可执行化" 10_版本演进/Roadmap.md || fail "Roadmap里程碑A缺失"

heading "YouYu参考工程一致性"
grep -Fq "YouYu版本：$youyu_release" README.md || fail "README YouYu版本不一致"
grep -Fq "youyu_release: $youyu_release" 12_框架项目Context/README.md || fail "Context YouYu版本不一致"
grep -Fq "YouYu版本：$youyu_release" 09_参考工程/README.md || fail "参考工程YouYu版本不一致"
grep -Fq "reference_release: $youyu_release" 12_框架项目Context/阶段/v0.2-A_Context可执行化.md || fail "阶段Context YouYu版本不一致"

heading "验证与成熟度一致性"
grep -Fq "youyu_formal_business_validation: $formal_validation" 12_框架项目Context/README.md || fail "Context正式业务验证状态不一致"
grep -Fq "正式业务验证：$formal_validation" README.md || fail "README正式业务验证状态不一致"
grep -Fq "Context模板：$context_maturity" README.md || fail "README Context成熟度不一致"
grep -Fq "数据库规范：$database_maturity" README.md || fail "README数据库成熟度不一致"
grep -Fq "Harness里程碑B：$harness_b" README.md || fail "README Harness B状态不一致"
grep -Fq "context_template_maturity: $context_maturity" 12_框架项目Context/README.md || fail "Context模板成熟度字段不一致"
grep -Fq "database_standard_maturity: $database_maturity" 12_框架项目Context/README.md || fail "数据库规范成熟度字段不一致"
grep -Fq "harness_milestone_b: $harness_b" 12_框架项目Context/README.md || fail "Harness B状态字段不一致"
grep -Fq "状态：\`$harness_b\`" 10_版本演进/Roadmap.md || fail "Roadmap Harness B状态不一致"

heading "AGENTS动态状态防漂移"
if grep -Eq '当前稳定版本：v[0-9]+\.[0-9]+\.[0-9]+' AGENTS.md; then
  fail "AGENTS不得声明动态当前稳定版本"
fi
if grep -Eq '当前工作段：|YouYu版本：v[0-9]+' AGENTS.md; then
  fail "AGENTS不得维护动态工作段或YouYu版本"
fi
grep -Fq '当前稳定版本只从根目录 `VERSION` 读取' AGENTS.md || fail "AGENTS缺少版本事实源规则"
grep -Fq 'Framework 项目 Context' AGENTS.md || fail "AGENTS缺少动态状态唯一入口"

heading "发布状态一致性检查完成"
printf 'Framework %s、YouYu %s、目标 %s、里程碑A和成熟度状态一致。\n' "$release_tag" "$youyu_release" "$target_release"
