# 阶段 Context

> 模板状态：`candidate` / 候选。阶段名称必须映射 Framework 十阶段生命周期。

中文术语遵循：[术语与易懂表达规范](../../01_框架定义/术语与易懂表达规范.md)。

```yaml
stage_context_id:
stage_context_pack_version:
project:
stage:
status: preparing
record_status: current
owner:
reviewer:
human_approver:
started_at:
project_context_pack_version:
baseline_commit:
source_commit:
last_verified_at:
supersedes:
superseded_by:
review_triggers:
  - project_stage_changed
  - task_completed_or_blocked
  - human_approval_recorded
  - pull_request_merged_closed_or_reverted
  - release_or_reference_baseline_changed
expires_when:
  - 项目Context的current_stage与本文件stage不一致
  - 出现影响阶段结论的新证据且尚未复核
```

> `status` 使用统一阶段状态枚举；`record_status` 使用 `current`、`archived` 或 `superseded`；`stage_context_pack_version` 与 `project_context_pack_version` 不得混用。

## 1. 阶段身份

- 当前阶段：
- 当前状态：`not_started` / `preparing` / `active` / `in_review` / `approved` / `blocked` / `stopped`
- 中文显示：未开始 / 准备中 / 进行中 / 待评审 / 已通过 / 已阻塞 / 已停止
- 阶段负责人：
- 审查人：
- 人工批准人：
- 计划进入时间：
- 目标退出时间：

### 新鲜度与替代关系

- 最近确认日期：
- 最近确认所依据的提交：
- 替代的阶段 Context：
- 被哪个阶段 Context 替代：
- 触发复核的事件：
- 何时不得继续作为当前事实使用：

## 2. 进入依据

| 输入或结论 | 权威来源 | 来源版本或提交 | 状态 | 批准人 |
|---|---|---|---|---|

### 上一阶段退出结论

### 允许带入的风险

### 尚未满足的前置条件

## 3. 阶段目标

### 本阶段要消除的关键不确定性

### 本阶段不解决的问题

### 与产品目标的关系

## 4. 必须产物

| 产物 | 目标 | 权威路径 | 责任人 | 依赖 | 状态 | 验证或批准方式 |
|---|---|---|---|---|---|---|

## 5. 阶段内工作边界

### 允许开展

### 禁止提前开展

### 可并行任务

### 必须串行的依赖

### 人工确认点

## 6. 风险、阻塞和未决事项

| 类型 | 内容 | 影响 | 是否阻塞 | 临时处理 | 决策人 | 截止条件 |
|---|---|---|---|---|---|---|

## 7. 阶段任务索引

| 任务 ID | 任务 | 责任人或 Agent | 状态 | Context Pack | 依赖 |
|---|---|---|---|---|---|

## 8. 退出检查关卡

- [ ] 必要输入为当前有效版本；
- [ ] 必须产物已经完成；
- [ ] 必须产物已经审查或批准；
- [ ] 关键冲突已经解决；
- [ ] 阻塞项已经关闭；
- [ ] 剩余风险在允许范围；
- [ ] 下一阶段依赖已经准备；
- [ ] 项目 Context Pack 已同步长期变化；
- [ ] 项目 Context、阶段索引和本文件指向同一当前阶段；
- [ ] `source_commit`、`last_verified_at` 和 Pack 版本已更新；
- [ ] 复核触发事件已逐项判断；
- [ ] 历史阶段已归档并链接当前阶段；
- [ ] 人工批准人确认退出。

## 9. 退出证据

| 检查关卡 | 证据 | 结果 | 验证人 | 日期 |
|---|---|---|---|---|

## 10. 退回路径

| 触发条件 | 退回阶段 | 需要重新确认的内容 | 决策人 |
|---|---|---|---|

## 11. 阶段结论

- 结论：通过 / 有条件通过 / 退回 / 停止
- 机器状态：`approved` / `active` / `blocked` / `stopped`
- 批准人：
- 日期：
- 条件或限制：
- 下一阶段：
- 需要回写的长期事实：

## 12. 更新记录

| 日期 | 变化 | 修改人 | 关联任务、提交或决策 |
|---|---|---|---|

> 项目阶段变化、任务完成或阻塞、人工批准、PR 合并或关闭、版本或参考基线变化时，即使阶段名称不变，也必须新增一条复核记录。
