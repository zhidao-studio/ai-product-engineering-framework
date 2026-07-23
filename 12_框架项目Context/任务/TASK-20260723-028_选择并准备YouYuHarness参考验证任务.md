# TASK-20260723-028：选择并准备 YouYu Harness 参考验证任务

```yaml
task_id: TASK-20260723-028
task_context_pack_version: 1.0
title: 选择并准备YouYu Harness参考验证任务
status: completed
project: AI Product Engineering Framework
lifecycle_stage: 质量与安全验证
risk_level: medium
owner: zhidao-studio
executor: Codex
reviewer: Codex
human_approver: 项目维护者
project_context_pack_version: 0.2-B.5
stage_context_pack_version: 1.0
source_commit: fd6095d46a4abacc7721a6069aeab73aee20c9fd
created_at: 2026-07-23
```

## 1. 目标

基于 YouYu 当前真实状态选择一个新的 Harness 参考任务，并建立可执行任务 Context、边界、一致性矩阵、证据计划和失败停止方式。

## 2. 允许动作

- 只读检查 Framework 与 YouYu 当前事实；
- 在 Framework 记录选择依据和状态；
- 选择完成后，在 YouYu 建立正式任务与控制资产；
- 执行不改变外部状态的环境和基线检查。

## 3. 禁止动作

- 正式任务建立前修改 YouYu 业务代码；
- 自动批准产品范围、高保真和敏感数据；
- 修改生产配置、真实凭据或外部平台；
- 跳过任务边界直接开始实现；
- 提升 Framework 版本和候选资产成熟度。

## 4. 验收断言

- [x] YouYu 当前 Context 和代码基线经过只读复核；
- [x] 参考任务有真实用户或运行价值；
- [x] 任务规模足以验证 B1 至 B3，但不会扩大成新产品阶段；
- [x] YouYu 正式任务 Context 与控制清单建立；
- [x] 三层证据和人工确认点明确；
- [x] 未提前形成参考验证通过结论。

## 5. 当前状态

已选择 YouYu TASK-016，并在提交 `00900d2b` 建立工程设计、任务 Context、控制清单、证据清单和状态回写。准备检查见 [HARNESS-REF-PREP-001](../验证/HARNESS-REF-PREP-001_YouYu网络来源频控参考任务准备.md)。

最终状态：`completed`。参考任务实现仍为 `not_started`。
