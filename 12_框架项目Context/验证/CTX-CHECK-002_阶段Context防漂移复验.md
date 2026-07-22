# CTX-CHECK-002：阶段 Context 防漂移复验

```yaml
check_id: CTX-CHECK-002
status: completed
result: passed_current_stage_revalidation_with_transition_pending
framework_task: TASK-20260722-023
framework_baseline_commit: 04d09ac0e5318b6794b4f9d23554c8c3328be4f2
reference_project: YouYu
reference_source_commit: 50d9a1b6e110fbe2f64fb89a1cdbca00ab13d474
reference_task: TASK-015
verified_at: 2026-07-22
verifier: Codex
human_approver: 项目维护者（仅保留里程碑 A 退出批准，本检查不代替该批准）
```

## 1. 检查目标

验证修订后的阶段 Context 规范能否识别并修复 YouYu 的真实阶段漂移，使项目 Context、阶段索引、当前阶段、历史阶段和任务状态重新一致。

## 2. 缺陷基线

2026-07-18 至 2026-07-22：

- YouYu `项目Context.md` 有 23 次提交；
- YouYu `05_项目Context/阶段/` 有 0 次提交；
- 项目 Context 已进入“质量与安全验证”，阶段索引仍指向 `status: active` 的“业务功能准备阶段”；
- 任务完成、维护者真机批准和 PR #3 合并均未触发阶段 Context 复核。

统计范围、命令和限制见 YouYu `EXP-005_账号与我Context成本和阶段漂移.md`。Token、人工工时和模型或工具费用均为 `not_measured`，没有使用估算值替代事实。

## 3. 修订内容

- 规范和模板增加 `record_status`、`source_commit`、`last_verified_at`；
- 增加 `supersedes`、`superseded_by`；
- 增加 `review_triggers` 和 `expires_when`；
- 规定项目阶段变化、任务完成或阻塞、人工批准、PR 合并或关闭、版本或参考基线变化必须触发复核；
- 完整性检查清单增加项目、索引、阶段一致性和历史替代检查。

## 4. YouYu 复验结果

| 检查项 | 证据 | 结果 |
|---|---|---|
| 当前阶段一致 | 项目 Context、阶段 README、`质量与安全验证阶段.md` | 通过 |
| 历史阶段不参与当前装配 | `业务功能准备阶段.md` 为 `record_status: archived` | 通过 |
| 来源与最近确认 | 当前阶段包含完整 `source_commit` 和 `last_verified_at` | 通过 |
| 替代关系 | 新阶段 `supersedes` 旧阶段，旧阶段 `superseded_by` 新阶段 | 通过 |
| 更新触发 | 当前阶段列出任务、批准、PR、阶段和版本变化 | 通过 |
| 核心路径与专项边界 | 当前阶段保留八类未完成专项和发布限制 | 通过 |
| Context 成本记录 | EXP-005 记录可复算指标、至少 8 个修正事件和不可测量项 | 通过 |
| 业务代码边界 | TASK-015 仅修改文档和 Context | 通过 |

## 5. 成熟度判断

阶段模板继续保持 `candidate`，原因不是复验失败，而是修订后的触发机制只在 YouYu 当前阶段完成了一次回溯修复与当前状态复验，尚未观察下一次真实阶段转换能否按触发规则及时归档和更新。

当前可作出的结论：

```text
候选模板结构已在一个真实项目当前阶段复验通过
≠ 已完整经历一次修订后的阶段进入与退出
≠ single_project_validated
≠ cross_project_validated 或 stable
```

## 6. A2 判断

TASK-20260722-023 已补齐 Context 成本、主要人工修正、阶段漂移修订和当前阶段复验。A2 的工程退出条件已经具备证据，唯一保留条件是维护者明确批准里程碑 A 退出。

Harness B 继续为 `not_started`；维护者批准 A 退出也不自动等于批准启动 B。

## 7. 未覆盖范围

- 下一次真实阶段变化是否按触发规则及时执行；
- 自动化防漂移检查；
- 冲突和经验回写模板的完整关闭复验；
- 跨项目证据；
- GitHub Billing 与计划额度检查（维护者决定暂缓）。
