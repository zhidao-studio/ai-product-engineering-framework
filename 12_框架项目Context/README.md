# AI 产品工程框架：项目 Context Pack

> 本文件是 `ai-product-engineering-framework` 当前运行状态、阻塞、风险和下一步的唯一入口。README、AGENTS、Roadmap、历史任务、验证和发布报告只提供摘要或历史证据，不得覆盖本文件的当前状态。

```yaml
project_context_id: PROJ-CONTEXT-AIPEF
project: AI Product Engineering Framework
status: active
execution_status: active
context_pack_version: 0.2-A.12
owner: zhidao-studio
current_stage: 工程规格设计
current_work_segment: A2 / YouYu 高保真确认与工程规格准备
stable_release: v0.1.6
target_release: v0.2.0
current_milestone: A / Context 可执行化
working_branch: main
source_commit: 72d06728245626ae33454b4e2e85730ac608a98f
youyu_engineering_review_result_commit: c656ea0e93696fc1a5ad5e24364f2b96d5dcf6ef
youyu_engineering_fix_commit: 9aff6d5768442da9530c2547d658eec3aa96be2c
youyu_ci_result_commit: 25f5e9bd138d0ae4fba0e2552d0298f186d6ee8a
youyu_business_preparation_commit: 70dffe94b4c6330e97eecb8afe9d83004092dd81
youyu_database_standard_adoption_commit: f102deefb0cd2d2fa503be33f9b7fae4d9b9e7b7
youyu_high_fidelity_candidate_commit: de87462b57585ef89756c2354f74710da648692e
youyu_high_fidelity_validation_commit: 1905feed1e2b4b2bf38c62aa3d7c72d6102d2a38
youyu_prototype_automation_commit: 439fbeacc9aaadb9adb9d1a88aa6bbb8571377ab
youyu_state_commit: 5a5644070af1396dced58c1ec2808ede3126db89
repository_visibility: public_pending_private
license_model: proprietary_all_rights_reserved
last_verified_at: 2026-07-15
sensitivity: proprietary
```

> `source_commit` 是本次同步开始时已经核验的 Framework `main` 基线。YouYu 的工程复核、修复、远程检查、数据库规范采用、高保真候选、候选检查和自动检查分别使用独立提交字段固定；它们均不代替正式业务实现或正式业务验证结论。

## 1. 当前结论

| 项目 | 当前结论 |
|---|---|
| 稳定版本 | v0.1.6，本次不发布新稳定版本 |
| 目标版本 | v0.2.0 |
| 当前里程碑 | A / Context 可执行化 |
| 当前工作段 | A2 / YouYu 高保真确认与工程规格准备 |
| 当前执行状态 | `active` |
| YouYu 工程基础 | `conditional_pass`；本地真机和远程重复构建证据已具备 |
| 首个正式业务切片 | 手机号验证码登录注册与个人资料管理，已确认 |
| 产品定义 | `completed` |
| 体验定义 | `confirmed` |
| 数据库基础规范 | YouYu 已采用；Framework 中为 `candidate` |
| 高保真候选 | `v0.1.0-draft.5`，检查 `conditional_pass`，待维护者逐页批准 |
| YouYu 正式业务实现 | `blocked` |
| YouYu 正式业务验证 | `not_started` |
| Context 模板成熟度 | `candidate` |
| Harness 里程碑 B | 尚未正式开始 |
| 仓库可见性 | GitHub 已核验为 Public，待维护者手动切换 Private |

## 2. A1 与 A2 进度

### A1：规范、候选模板与 Framework 自应用

状态：`completed`

已完成四级 Context、独立回写层、事实源与状态、装配与冲突、完整性检查、五类候选模板和 Framework 自应用。历史自应用评分为 93/100，但不代表候选模板已经通过正式业务项目验证。

### A2：正式业务参考工程验证准备

状态：`active`

已完成：

- YouYu 产品工程目录、项目 Context、工程设计、接口与数据约定入口、检查关卡、测试验收和部署运维入口；
- `YouYu-iOS/` 确认为唯一正式 iOS 工程，并正式放弃 mPaaS；
- iOS 真机 Debug 构建、安装和启动，服务地址改为构建配置注入；
- 服务端 Maven 构建、App/Gateway 基础接口验证、短时签名内部身份传递及单元测试；
- 采集工程依赖修复和构建；
- GitHub Actions 服务端、采集工程和 iOS 远程重复构建检查；
- 首个正式业务切片选择、产品范围、业务规则和验收断言；
- 用户流程、信息架构、页面清单和交互说明确认；
- YouYu 统一数据库基础规范采用，Framework 候选数据库规范登记；
- HTML 高保真候选 `v0.1.0-draft.5`，并形成 `conditional_pass` 候选检查；
- 高保真主导航与正式 iOS 工程对齐，删除未建设空入口，清理重复业务规则和用户流程事实源；
- 候选原型增加 JavaScript、JSON、范围、权威来源和静态页面访问自动检查。

尚未完成：

- 维护者逐页批准 `v0.1.0-draft.5`；
- 账号、个人资料和验证码业务表及既有表差异清单；
- 登录、退出、当前用户、资料修改和账号信息 OpenAPI；
- 错误码、示例数据和客户端字段映射；
- iOS、服务端和数据库实现任务边界；
- Git 历史敏感信息轮换、历史清理和扫描检查关卡；
- 共享会话存储和下游网络隔离运行验证；
- 采集候选数据、人工审核和正式数据隔离的运行控制；
- iOS 测试/生产环境、真机明暗模式、断网和服务异常人工验收；
- 正式项目、阶段和任务 Context；
- 受控业务实现、静态验证、运行验证和模拟用户验收；
- Context 成本、人工修正、遗漏和任务成本复盘；
- 模板成熟度升级判断和里程碑 A 人工退出批准。

## 3. 项目身份与边界

- **仓库**：`zhidao-studio/ai-product-engineering-framework`；
- **定位**：由 zhidao-studio 专有维护、跨平台、可验证的 AI 产品工程框架；
- **默认分支**：`main`；
- **稳定版本边界**：本次只同步 v0.2.0 未发布开发进度，不修改 `VERSION`，不发布 v0.1.7；
- **明确不做**：当前不建设通用向量知识库、自动记忆平台、完整 Skill 市场、无人值守 Agent 编排或未经验证的企业级治理平台。

## 4. 权威事实入口

| 主题 | 权威来源 |
|---|---|
| 许可与外部使用 | [LICENSE](../LICENSE) / [DEC-009](../11_设计决策/DEC-009_采用专有闭源许可并限制未经授权使用.md) |
| 愿景、原则与边界 | [框架定义](../01_框架定义/AI产品工程框架愿景与定位.md) |
| 三平面和十阶段 | [全局框架](../02_全局模型/AI产品工程全局框架.md) |
| Context 工程 | [Context 工程](../04_Context工程/README.md) |
| Harness 当前定义 | [执行控制与检查关卡](../05_Harness工程/执行控制与检查关卡.md) |
| 数据库候选规范 | [数据库设计基础规范](../08_模板资产/工程规格/数据库设计基础规范.md) |
| 版本规则与路线 | [版本管理规范](../10_版本演进/版本管理规范.md) / [Roadmap](../10_版本演进/Roadmap.md) |
| 当前阶段详情 | [v0.2.0 / A 阶段 Context](阶段/v0.2-A_Context可执行化.md) |
| 当前参考工程状态 | [参考工程入口](../09_参考工程/README.md) |

## 5. 当前任务与证据

| 任务 | 状态 | 入口 |
|---|---|---|
| v0.1.5 当前状态收敛与历史边界治理 | `completed` | [TASK-20260712-007](任务/TASK-20260712-007_发布v0.1.5并收敛当前状态.md) |
| 同步 YouYu 工程基础复核进度 | `completed` | [TASK-20260713-008](任务/TASK-20260713-008_同步YouYu工程基础复核进度.md) |
| 同步工程基础复核结论并进入基础问题关闭 | `completed` | [TASK-20260714-009](任务/TASK-20260714-009_同步YouYu工程基础复核结论并进入基础问题关闭.md) |
| 发布 v0.1.6 并同步工程修复与业务准备 | `completed` | [TASK-20260714-010](任务/TASK-20260714-010_发布v0.1.6并同步YouYu工程修复与业务准备.md) |
| 同步 YouYu 产品体验与高保真候选进度 | `completed` | [TASK-20260715-011](任务/TASK-20260715-011_同步YouYu产品体验与高保真候选进度.md) |
| YouYu TASK-008 高保真人工确认 | `in_review` | YouYu 仓库 `05_项目Context/任务/TASK-008_建设账号与个人中心高保真候选原型.md` |
| 关闭 YouYu 工程基础 P0 阻塞 | `blocked` | YouYu 仓库 `05_项目Context/任务/TASK-004_关闭工程基础P0阻塞.md` |
| 正式业务实现任务 | `not_created` | 高保真、工程规格和阻塞条件满足后创建 |

当前有效证据包括 YouYu 工程基础复核、远程构建、数据库规范采用、`v0.1.0-draft.5` 高保真候选、HIFI-CHECK-001 和候选原型自动检查。YouYu PR #1、REF-CHECK-001 及早期 `partial_pass` 只保留为历史证据。

## 6. 风险与阻塞

| 风险或事项 | 是否阻塞 | 当前处理 | 下一决策点 |
|---|---|---|---|
| Framework 仓库仍为 Public | 阻塞真正访问控制 | 已有专有许可，待维护者切换 Private | 立即执行 |
| 高保真尚未人工批准 | 阻塞客户端实现依据 | `draft.5` 已达人工评审条件 | 维护者逐页确认后 |
| 接口和业务数据结构未完成 | 阻塞联合设计与实现 | 下一步建立表、OpenAPI、错误码和映射 | 工程规格确认后 |
| Git 历史敏感信息 | 阻塞安全结论 | 轮换凭据、清理历史并建立扫描检查关卡 | SECURITY-001 关闭后 |
| 共享会话与下游网络隔离未验证 | 阻塞正式业务实现 | 已有身份签名单元测试，继续运行验证 | 专项安全任务完成后 |
| 采集待审入库控制缺失 | 阻塞真实采集链路 | 建立候选、审核、正式数据隔离运行证据 | 专项采集任务完成后 |
| iOS 视觉与环境验证未完成 | 阻塞用户体验结论 | 工程可构建，待真机截图和异常验收 | TASK-006 完成后 |
| 正式业务验证尚未开始 | 阻塞模板成熟度升级 | 保持 `candidate` | 里程碑 A 退出前 |
| Context 成本与人工修正数据缺失 | 阻塞模板成本判断 | 正式任务中记录 | 里程碑 A 退出前 |
| PR 人工检查关卡未约束实际合并 | 阻塞检查关卡可信性 | 里程碑 B 建 Required Checks | Harness 可执行化 |

## 7. 下一步

```text
维护者逐页批准 YouYu v0.1.0-draft.5
→ 设计账号、资料和验证码业务表及既有表差异
→ 建立 OpenAPI、错误码、示例数据和客户端字段映射
→ 并行关闭或形成可审计隔离结论：安全、共享会话、网络隔离、采集待审和 iOS 真机体验
→ 建立正式 YouYu 项目、阶段和任务 Context
→ 配置修改边界、检查关卡和人工确认节点
→ 执行业务实现并完成静态、运行和模拟用户三层验证
→ 记录成本、遗漏、冲突和人工修正
→ 回写 Framework，判断候选资产成熟度和里程碑 A 是否退出
```

在高保真批准、工程规格完成和正式实现阻塞具备证据前，不启动正式业务代码实现，不提前宣布进入 Harness B，也不升级候选模板或数据库规范成熟度。

## 8. 安全与敏感信息

- 本仓库内容属于专有资产；
- 不得提交密钥、凭据、个人隐私或未授权企业信息；
- 示例数据必须使用合成或脱敏内容；
- 临时外网地址不得作为稳定发布地址或长期事实源；
- 未经书面授权，不得将仓库内容发送到外部模型、第三方知识库、公共数据集或其他仓库；
- 删除当前文件不等于关闭历史凭据风险，必须轮换凭据、检查访问、清理 Git 历史并建立扫描检查关卡。

## 9. 更新记录

| 日期 | 变化 | 关联决策或任务 |
|---|---|---|
| 2026-07-12 | 建立 Framework 自身项目 Context Pack并完成治理修订 | DEC-007 至 DEC-010 / TASK-001 至 TASK-007 |
| 2026-07-13 | YouYu 进入工程基础复核 | TASK-20260713-008 |
| 2026-07-14 | YouYu 工程修复和远程检查完成，进入业务功能准备 | TASK-20260714-009 / TASK-20260714-010 / v0.1.6 |
| 2026-07-15 | YouYu 产品和体验完成，高保真 `draft.5` 进入人工确认，数据库候选规范与原型自动检查完成同步 | TASK-20260715-011 |
