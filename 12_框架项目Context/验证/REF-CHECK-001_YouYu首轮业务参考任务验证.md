# REF-CHECK-001：YouYu 首轮业务参考任务验证

> **历史快照：** 本文件记录 YouYu PR #1 在 2026-07-12 当时形成的初步工程证据和 `partial_pass` 判断。后续 [TASK-20260712-006](../任务/TASK-20260712-006_修正YouYu正式验证状态.md) 已明确：该 PR 不属于 Framework v0.2.0 / A 的正式业务参考工程验证，当前正式验证状态为 `not_started`。当前状态以 [Framework 项目 Context](../README.md) 和 [参考工程入口](../../09_参考工程/README.md) 为准。

```yaml
validation_id: REF-CHECK-001
project: AI Product Engineering Framework
reference_project: zhidao-studio/YouYu
reference_task: 钓点详情风险摘要与风险抽屉
status: partial_pass
maturity_result: candidate
framework_release: v0.1.2
target_release: v0.2.0
milestone: A / Context 可执行化
reviewed_at: 2026-07-12
reviewer: Framework 全量 Review
human_approver: zhidao-studio
```

> 上述 `status: partial_pass` 仅表示当时对 PR #1 工程证据的历史判断，不等于当前正式业务参考工程状态。

## 1. 验证目标

确认 YouYu 的真实 iOS 业务任务是否能够作为 Framework v0.2.0 / A 的首个业务参考工程证据，并据此判断：

- 项目、阶段和任务 Context 是否在真实任务中被使用；
- 修改边界和工程门禁是否产生实际约束；
- 是否完成静态、运行和模拟用户三层验证；
- Context 候选模板是否具备升级为 `single_project_validated` 的证据；
- 哪些问题需要回写 Framework 和后续 Harness。

## 2. 权威证据

- 业务仓库：`zhidao-studio/YouYu`；
- Pull Request：[验证：钓点风险 Context、mPaaS 路由与真机架构门禁](https://github.com/zhidao-studio/YouYu/pull/1)；
- PR 合并提交：`9adaeca0259457c1e10609733a78102548c1a47c`；
- PR 状态：已合并；
- PR 自述状态：`Draft / awaiting_device_user_acceptance`；
- PR 自述未通过门禁：`GATE-005` 签名真机模拟用户验收。

## 3. 已获得的验证证据

### 3.1 Context 使用

PR 记录显示已经建立：

- 项目 Context；
- 阶段 Context；
- 任务 Context；
- 实时状态记录。

这证明四级 Context 中的项目、阶段和任务三层已经进入真实业务修改，不再仅是 Framework 自应用。

> 后续复核说明：这些材料证明了 Context 概念在一次真实代码修改中的初步使用，但不能证明整理后的正式项目基线和完整业务链路。

### 3.2 修改边界

PR 明确声明未修改：

- 后端和数据库；
- 地图、导航和直播；
- 动态、评论和发布；
- 鉴权和媒体协议；
- 历史工程；
- 业务 Pod 依赖。

这提供了任务范围和禁止修改边界的真实使用证据。

### 3.3 工程门禁

PR 记录以下门禁已经通过：

- `GATE-001`：Xcode 源码注册完整性；
- `GATE-002`：Xcode 资源注册完整性；
- `GATE-003`：mPaaS 真机架构构建；
- `GATE-004`：mPaaS Debug 风险路由。

同时形成了以下可复用 Harness 候选问题：

- 源码文件存在但未注册到真实 Target；
- Assets 或资源存在但未进入构建阶段；
- 依赖只能在真机架构构建，模拟器验证会产生错误结论；
- Debug 验证入口与 Release 默认入口需要隔离；
- 生成代码、工程注册和运行路由需要保持一致。

## 4. 未完成的验证

### 4.1 模拟用户验收未完成

PR 明确记录 `GATE-005` 尚未通过，缺少：

- Apple 开发签名真机启动；
- 首个 Tab 展示钓点详情；
- 第一屏风险摘要检查；
- 风险抽屉打开、关闭和上下文保持；
- 小屏、暗黑模式和动态字体；
- VoiceOver；
- 截图和录屏证据；
- P0/P1 体验问题关闭。

因此三层验证中的“模拟用户验收”没有完整证据。

### 4.2 产品生命周期证据不完整

当前证据主要集中在受控执行和工程验证，尚未完整证明：

- 战略与价值验证；
- 已批准的产品定义和不做清单；
- 用户体验设计与高保真人工确认；
- 前后端 API 与数据库契约；
- 发布交付；
- 真实运行反馈与产品 Loop。

### 4.3 Context 效率指标缺失

尚未记录：

- Context Pack 填写时间；
- 新 Agent 恢复背景所需时间；
- 人工修正次数和比例；
- Context 冲突、遗漏和过期数量；
- 哪些字段有效、重复或过重；
- 任务 Token、时间和人工成本。

## 5. 发现的流程问题

PR 正文明确写明：在 `GATE-005` 通过并由维护者确认前不得合并到 `main`，但该 PR 后续实际已经合并。

这不是业务代码正确性结论，而是一个重要 Harness 缺陷：

> 文档中的人工门禁和 PR 的实际合并权限没有形成强制约束。

需要在里程碑 B 评估以下机制：

1. PR 状态与任务状态一致性检查；
2. `pending_human_approval` 或 `awaiting_device_user_acceptance` 时禁止合并；
3. 必需门禁列表与 GitHub Branch Protection/Required Checks 映射；
4. 人工批准记录必须在合并前存在；
5. 合并后发现门禁缺失时自动形成异常记录，而不是静默视为完成。

## 6. 成熟度结论

| 资产 | 当前结论 | 原因 |
|---|---|---|
| 项目 Context Pack | `candidate` | 已有真实使用证据，但恢复效率和完整闭环未验证 |
| 阶段 Context | `candidate` | 已用于任务组织，但阶段退出和退回路径未完整验证 |
| 任务 Context Pack | `candidate` | 边界和门禁产生了实际价值，但人工验收和成本数据缺失 |
| Context 冲突记录模板 | `candidate` | 本任务没有形成完整冲突样例 |
| 经验回写模板 | `candidate` | 本报告形成首次回写，但尚未完成跨任务复验 |

本次历史结果为 `partial_pass`。不得把任何 Context 模板升级为 `single_project_validated`。

后续 TASK-006 进一步确认：由于 YouYu 基础框架仍在整理，该结果不得计入正式业务参考工程启动或部分通过。

## 7. 对 Framework 的回写

本次验证当时要求同步：

- 将“业务参考工程尚未开始”修正为“首轮部分验证已完成”；
- 保持 Context 模板成熟度为 `candidate`；
- 将签名真机验收、Context 成本复盘和人工修正统计列为里程碑 A 剩余门禁；
- 将 PR 合并状态与人工门禁不一致纳入 Harness 里程碑 B；
- 将 Xcode 源码注册、资源注册、真机架构和运行路由检查列为候选门禁；
- 后续使用一个包含前端、后端、API 和数据库的完整业务切片验证端到端契约。

其中第一项已被后续 TASK-006 修正：当前正式业务参考工程状态为 `not_started`，PR #1 只保留为初步工程证据。

## 8. 下一步

以下是本文件形成时的历史计划：

1. 在可签名真机环境完成 `GATE-005`；
2. 补充模拟用户验收证据和 P0/P1 关闭记录；
3. 对本次 Context 使用进行填写成本、遗漏和人工修正复盘；
4. 根据结果决定是否完成里程碑 A；
5. 进入 Harness 里程碑 B，优先实现门禁状态与实际合并行为的一致性控制；
6. 选择前后端完整业务切片继续验证 OpenAPI、Schema、依赖和联调门禁。

当前下一步已调整为：等待 YouYu 基础框架整理完成后，重新复核 `main` 并建立正式项目、阶段和任务 Context。详见 [Framework 项目 Context](../README.md)。
