# TASK-20260723-029：跟踪 YouYu TASK-016 并验证 Harness

```yaml
task_id: TASK-20260723-029
status: in_progress
project: AI Product Engineering Framework
lifecycle_stage: 受控任务执行
risk_level: high
owner: zhidao-studio
executor: Codex
reviewer: Codex
human_approver: 项目维护者
project_context_pack_version: 0.2-B.6
stage_context_pack_version: 1.0
source_commit: a6715ef
youyu_task: TASK-016
youyu_task_commit: 00900d2b
created_at: 2026-07-23
```

## 1. 目标

跟踪 TASK-016 的分点实现、检查、失败和用户回归，并用真实证据判断 Harness B1 至 B3 的候选能力是否有效。

## 2. Framework 允许修改

- 当前阶段、任务、参考检查和项目 Context；
- Harness 候选资产中被真实问题证明需要修订的部分；
- Roadmap、README 和 CHANGELOG 的事实同步。

## 3. 禁止

- 用 Framework 状态代替 YouYu 真实执行；
- 在失败证据产生前预写 `passed`；
- 自动提升版本或资产成熟度；
- 替维护者批准生产代理、密钥、发布或安全豁免。

## 4. 需要收集

- 每个 YouYu 提交和对应验证；
- 边界、一致性、证据检查的实际结果；
- 首次失败、重试次数和停止判断；
- 规则带来的实际成本；
- 用户回归和维护者结论；
- 可复用反馈及其适用范围。

## 5. 当前状态

TASK-016 已完成准备并推送，真实实现和验证尚未开始。
