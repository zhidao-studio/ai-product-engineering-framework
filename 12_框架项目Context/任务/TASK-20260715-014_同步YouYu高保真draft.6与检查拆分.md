# TASK-20260715-014：同步 YouYu 高保真 draft.6 与检查拆分

```yaml
task_id: TASK-20260715-014
status: completed
project: AI Product Engineering Framework
stage: 工程规格设计
work_segment: A2 / YouYu 高保真确认与工程规格准备
risk_level: medium
owner: zhidao-studio
executor: ChatGPT
created_at: 2026-07-15
framework_baseline_commit: ae24425af446390fbaa49b0b6810dba299ecc376
youyu_repository_head_at_review: b3ce14c09ff3dd0d3250e72c836ba428785178b7
youyu_high_fidelity_candidate_commit: 3d8fd0499634da5e563c9a09644a456734131051
youyu_high_fidelity_validation_commit: 7e0e93a392acd5e2468701aee13e0df1bfb1418c
youyu_prototype_automation_commit: 99d651328939dddb30911b724ddb9b9a77df9c88
youyu_state_commit: 36c4d1161bb1d33b093d51b6f07145e1ac33a190
youyu_repository_head_at_sync: 7fce74b55dd4ed0c65165bb1f55abb9c42e444c6
stable_release: v0.1.6
release_changed: false
```

## 1. 目标

同步 YouYu 在全局复核后的真实进度，修正 Framework 对高保真版本、协议确认状态和自动检查结构的记录，不发布新的稳定版本，不提升候选资产成熟度。

## 2. 已核验事实

- YouYu 高保真候选已更新为 `v0.1.0-draft.6`；
- 登录页覆盖“需要确认当前协议版本”和“已确认当前协议版本、无需重复勾选”两种候选状态；
- 主导航继续与正式 iOS 工程一致，未建设空入口和重复事实源保持清理状态；
- 候选原型检查已从完整工程检查中拆分为独立轻量工作流；
- 完整工程检查改为按代码路径触发，避免产品和高保真文档变化重复消耗 Maven 与 macOS 构建资源；
- 新候选原型工作流检查版本、精确主导航、协议双状态、唯一事实源、本地静态引用和页面访问；
- GitHub Actions 账户账单或额度限制仍存在，维护者已决定暂缓远程成功证据；
- 高保真状态仍为 `draft_for_confirmation`，检查结论仍为 `conditional_pass`；
- 正式业务实现继续为 `blocked`，正式业务验证继续为 `not_started`。

## 3. Framework 边界

- Framework 稳定版本继续为 `v0.1.6`；
- Context 模板和数据库规范继续为 `candidate`；
- YouYu 项目级候选原型检查是参考工程实例，不等于 Harness 里程碑 B 已经开始或完成；
- 只有完成高保真批准、工程规格、受控实现和三层验证后，才判断候选资产成熟度。

## 4. 下一步

维护者逐页确认 YouYu `v0.1.0-draft.6`，随后设计账号、个人资料和验证码表、OpenAPI、错误码、示例数据、客户端字段映射及实现边界；同时继续处理安全、共享会话、网络隔离、采集待审和 iOS 真机体验阻塞。
