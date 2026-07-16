#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONTEXT_FILE="$ROOT_DIR/12_框架项目Context/README.md"
YOUYU_REPO_DIR="${YOUYU_REPO_DIR:-}"
cd "$ROOT_DIR"

fail() { printf 'ERROR: %s\n' "$1" >&2; exit 1; }
heading() { printf '\n==== %s ====\n' "$1"; }
require_file() { [[ -f "$1" ]] || fail "缺少文件: $1"; }
require_cmd() { command -v "$1" >/dev/null 2>&1 || fail "缺少命令: $1"; }

for file in VERSION README.md AGENTS.md CHANGELOG.md 10_版本演进/Roadmap.md \
  12_框架项目Context/README.md 12_框架项目Context/阶段/v0.2-A_Context可执行化.md \
  09_参考工程/README.md; do
  require_file "$file"
done
require_cmd git
require_cmd python3

context_value() {
  python3 - "$CONTEXT_FILE" "$1" <<'PY'
import re,sys
text=open(sys.argv[1],encoding='utf-8').read()
match=re.search(r'```yaml\s*(.*?)\s*```',text,re.S)
if not match:
    raise SystemExit('项目Context缺少yaml代码块')
key=sys.argv[2]
for line in match.group(1).splitlines():
    if line.startswith(key+':'):
        print(line.split(':',1)[1].strip())
        break
else:
    raise SystemExit(f'项目Context缺少字段: {key}')
PY
}

release="$(tr -d '[:space:]' < VERSION)"
[[ "$release" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || fail "VERSION格式错误: $release"
release_tag="v$release"
stable_release="$(context_value stable_release)"
target_release="$(context_value target_release)"
current_milestone="$(context_value current_milestone)"
current_work_segment="$(context_value current_work_segment)"
framework_source_commit="$(context_value source_commit)"
framework_baseline_commit="$(context_value baseline_commit)"
youyu_release="$(context_value youyu_release)"
youyu_source_commit="$(context_value youyu_source_commit)"
youyu_static_review="$(context_value youyu_static_review_status)"
formal_validation="$(context_value youyu_formal_business_validation)"
context_maturity="$(context_value context_template_maturity)"
database_maturity="$(context_value database_standard_maturity)"
harness_b="$(context_value harness_milestone_b)"

[[ "$stable_release" = "$release_tag" ]] || fail "VERSION与Context稳定版本不一致"

heading "提交真实性"
git cat-file -e "${framework_baseline_commit}^{commit}" 2>/dev/null || fail "Framework baseline_commit不存在: $framework_baseline_commit"
git cat-file -e "${framework_source_commit}^{commit}" 2>/dev/null || fail "Framework source_commit不存在: $framework_source_commit"
if [[ -n "$YOUYU_REPO_DIR" ]]; then
  [[ -d "$YOUYU_REPO_DIR/.git" ]] || fail "YOUYU_REPO_DIR不是Git仓库: $YOUYU_REPO_DIR"
  git -C "$YOUYU_REPO_DIR" cat-file -e "${youyu_source_commit}^{commit}" 2>/dev/null \
    || fail "YouYu source_commit不存在于指定仓库: $youyu_source_commit"
  [[ "$(tr -d '[:space:]' < "$YOUYU_REPO_DIR/VERSION")" = "${youyu_release#v}" ]] \
    || fail "YouYu VERSION与Framework参考版本不一致"
else
  printf 'INFO: 未设置YOUYU_REPO_DIR，只校验YouYu SHA格式，不宣称已验证其仓库归属。\n'
  [[ "$youyu_source_commit" =~ ^[0-9a-f]{40}$ ]] || fail "YouYu source_commit格式错误"
fi

heading "稳定版本与发布日期"
grep -Fq "当前稳定版本：$release_tag" README.md || fail "README稳定版本不一致"
python3 - CHANGELOG.md "$release" <<'PY'
import re,sys,datetime
text=open(sys.argv[1],encoding='utf-8').read()
version=re.escape(sys.argv[2])
m=re.search(rf'^## \[{version}\] - (\d{{4}}-\d{{2}}-\d{{2}})$',text,re.M)
if not m:
    raise SystemExit('CHANGELOG缺少当前版本发布段或日期')
datetime.date.fromisoformat(m.group(1))
PY
grep -Fq "| $release_tag | 已完成 |" 10_版本演进/Roadmap.md || fail "Roadmap缺少当前版本历史行"

heading "目标版本、里程碑与工作段"
grep -Fq "目标开发版本：$target_release" README.md || fail "README目标版本不一致"
grep -Fq "当前里程碑：$current_milestone" README.md || fail "README当前里程碑不一致"
grep -Fq "当前工作段：${current_work_segment// /}" README.md \
  || grep -Fq "当前工作段：$current_work_segment" README.md \
  || fail "README当前工作段不一致"
grep -Fq "### 里程碑 A：Context 可执行化" 10_版本演进/Roadmap.md || fail "Roadmap里程碑A缺失"

heading "YouYu参考工程一致性"
grep -Fq "YouYu版本：$youyu_release" README.md || fail "README YouYu版本不一致"
grep -Fq "YouYu版本：$youyu_release" 09_参考工程/README.md || fail "参考工程YouYu版本不一致"
grep -Fq "reference_release: $youyu_release" 12_框架项目Context/阶段/v0.2-A_Context可执行化.md || fail "阶段Context YouYu版本不一致"
grep -Fq "reference_source_commit: $youyu_source_commit" 12_框架项目Context/阶段/v0.2-A_Context可执行化.md || fail "阶段Context YouYu提交不一致"
grep -Fq "静态复核：$youyu_static_review" README.md || fail "README YouYu静态状态不一致"

heading "验证与成熟度一致性"
grep -Fq "正式业务验证：$formal_validation" README.md || fail "README正式业务验证状态不一致"
grep -Fq "Context模板：$context_maturity" README.md || fail "README Context成熟度不一致"
grep -Fq "数据库规范：$database_maturity" README.md || fail "README数据库成熟度不一致"
grep -Fq "Harness里程碑B：$harness_b" README.md || fail "README Harness B状态不一致"

python3 - 10_版本演进/Roadmap.md "$harness_b" <<'PY'
import re,sys
text=open(sys.argv[1],encoding='utf-8').read()
expected=sys.argv[2]
match=re.search(r'### 里程碑 B：.*?(?=\n### 里程碑 |\Z)',text,re.S)
if not match:
    raise SystemExit('Roadmap缺少里程碑B段落')
if f'状态：`{expected}`' not in match.group(0):
    raise SystemExit('Roadmap里程碑B状态不一致')
PY

heading "AGENTS动态状态防漂移"
if grep -Eq '当前稳定版本：v[0-9]+\.[0-9]+\.[0-9]+|当前工作段：|YouYu版本：v[0-9]+' AGENTS.md; then
  fail "AGENTS不得维护动态版本、工作段或参考工程版本"
fi
grep -Fq '当前稳定版本只从根目录 `VERSION` 读取' AGENTS.md || fail "AGENTS缺少版本事实源规则"
grep -Fq 'Framework 项目 Context' AGENTS.md || fail "AGENTS缺少动态状态唯一入口"

heading "发布状态一致性检查完成"
printf 'Framework %s、YouYu %s、目标 %s、里程碑与成熟度字段完成一致性检查。\n' \
  "$release_tag" "$youyu_release" "$target_release"
