# HARNESS-CHECK-002：B2 任务边界与依赖控制检查

```yaml
check_id: HARNESS-CHECK-002
status: passed
project: AI Product Engineering Framework
milestone: B / Harness 可执行化
work_segment: B2 / 任务边界与依赖控制
baseline_commit: ee8adf56036f952a7c75881c09e8ad30b8254225
implementation_commit: 44a6d1be1455ff2aadf43029abbad5e0062a9346
stable_release: v0.1.10
target_release: v0.2.0
verified_at: 2026-07-23
verifier: Codex
reference_validation: not_executed
asset_maturity: candidate
```

## 1. 检查范围

- 修改边界和权限规范；
- 依赖与高风险变更授权规范；
- Harness 候选模板和机器清单；
- `scripts/check_task_boundary.py`；
- TASK-20260723-026 的真实控制清单和工作区自应用。

## 2. 实际结果

| 检查 | 结果 | 证据 |
|---|---|---|
| Python 单元测试 | 9 项通过 | `python3 -m unittest scripts/tests/test_check_task_boundary.py` |
| JSON 结构 | 通过 | 两份控制清单可由 `json.tool` 解析 |
| Framework 工作区边界 | 11 个改动路径通过 | TASK-026 真实控制清单 |
| Markdown 本地链接 | 7 个 B2 文档通过 | 本地链接检查 |
| 发布状态一致性 | 通过 | `scripts/check-release-state.sh` |
| 空白和补丁检查 | 通过 | `git diff --check` |
| YouYu 新任务验证 | 未执行 | 后续工作段选择真实任务 |

## 3. 反向检查和修复

第一次真实工作区检查没有通过，发现两个实际问题：

1. Git 默认将中文路径输出为转义文本，脚本误判所有中文目录越界；
2. 测试产生 `__pycache__`，它不在允许范围内并被正确拦截。

处理结果：

- Git 命令显式使用 `core.quotePath=false`，保留真实中文路径；
- 清理本地 Python 缓存，后续验证使用 `PYTHONDONTWRITEBYTECODE=1`；
- 增加 `**/` 同时匹配根目录文件的测试；
- 重新执行后，9 项单元测试和 11 个真实改动路径全部通过。

该失败证明检查能够阻止未声明路径，而不是只提供始终成功的形式化脚本。

## 4. 证据边界

- 已证明：确定性 Git 路径、禁止范围、高风险路径和依赖文件授权可以检查；
- 未证明：代码语义、外部系统副作用、产品正确性或用户体验；
- 未证明：候选能力已在 YouYu 新任务中产生效果；
- 所有 B2 规范、模板和脚本成熟度继续为 `candidate`。

## 5. 结论

`passed`（仅限 B2 工程和 Framework 自应用范围）。可以进入下一工作段建设一致性、证据和失败停止控制；参考工程验证仍是 Harness B 后续退出条件。
