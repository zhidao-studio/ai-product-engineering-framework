# AI 产品工程框架：项目 Context Pack

> 本文件是 `ai-product-engineering-framework` 当前运行状态、阻塞、风险和下一步的唯一入口。README、AGENTS、Roadmap、历史任务、验证和发布报告只提供摘要或历史证据，不得覆盖本文件的当前状态。

```yaml
project_context_id: PROJ-CONTEXT-AIPEF
project: AI Product Engineering Framework
status: active
execution_status: active
context_pack_version: 0.2-A.17
owner: zhidao-studio
current_stage: 工程规格设计
current_work_segment: A2 / YouYu 高保真确认与工程规格基线
stable_release: v0.1.6
target_release: v0.2.0
current_milestone: A / Context 可执行化
working_branch: main
source_commit: 00b963f5f8505218eaabfa02c3a7b4ed22244b85
youyu_engineering_review_result_commit: c656ea0e93696fc1a5ad5e24364f2b96d5dcf6ef
youyu_engineering_fix_commit: 9aff6d5768442da9530c2547d658eec3aa96be2c
youyu_ci_result_commit: 25f5e9bd138d0ae4fba0e2552d0298f186d6ee8a
youyu_business_preparation_commit: 70dffe94b4c6330e97eecb8afe9d83004092dd81
youyu_database_standard_adoption_commit: f102deefb0cd2d2fa503be33f9b7fae4d9b9e7b7
youyu_high_fidelity_candidate_commit: 3d8fd0499634da5e563c9a09644a456734131051
youyu_high_fidelity_validation_commit: 7e0e93a392acd5e2468701aee13e0df1bfb1418c
youyu_prototype_automation_commit: 99d651328939dddb30911b724ddb9b9a77df9c88
youyu_prototype_remote_check_status: deferred_due_external_blocker
youyu_prototype_last_remote_check_status: blocked
youyu_prototype_last_remote_check_head_commit: fb55f154faa4af70c5785f66e4c3964cbaf9d14d
youyu_prototype_last_remote_check_run_id: 29408643569
youyu_prototype_remote_check_blocker: GitHub Actions 账户账单或额度限制，任务在执行前未启动
youyu_prototype_remote_check_follow_up: deferred_by_maintainer
youyu_engineering_specification_status: in_progress
youyu_engineering_gap_baseline_commit: 04ca345332b7b015a185b8e6362cd5917c61b694
youyu_candidate_data_model_commit: 7a3be9e7f9f672661a65820815e117f8832bc1d5
youyu_candidate_api_contract_commit: d365313c9b33209196446dd29dbcde1b4c0e4145
youyu_candidate_error_code_commit: aa56d434cb16a6c82d9538da9bdd393fa1f59981
youyu_candidate_field_mapping_commit: 22e048dea26a6e60a0a2a1444aa1cb7b66e4e9f7
youyu_existing_reference_scan_commit: b689002f3650a5b4ed52f60f0d0c0b9904737b36
youyu_state_commit: b689002f3650a5b4ed52f60f0d0c0b9904737b36
youyu_repository_head_at_sync: b689002f3650a5b4ed52f60f0d0c0b9904737b36
repository_visibility: public_pending_private
license_model: proprietary_all_rights_reserved
last_verified_at: 2026-07-15
sensitivity: proprietary
```

> `source_commit` 固定本轮 Framework 同步开始前的基线。YouYu 的工程复核、数据库规范、高保真候选、自动检查、工程差异、候选数据模型、候选接口和项目状态分别使用独立提交字段追溯；这些证据均不代替正式业务实现或正式业务验证结论。

## 1. 当前结论

| 项目 | 当前结论 |
|---|---|
| 稳定版本 | v0.1.6，本轮不发布新稳定版本 |
| 目标版本 | v0.2.0 |
| 当前里程碑 | A / Context 可执行化 |
| 当前工作段 | A2 / YouYu 高保真确认与工程规格基线 |
| YouYu 工程基础 | `conditional_pass` |
| 首个业务切片 | 手机号验证码登录注册与个人资料管理，已确认 |
| 产品定义 | `completed` |
| 体验定义 | `confirmed` |
| 数据库基础规范 | YouYu 已采用；Framework 中为 `candidate` |
| 高保真候选 | `v0.1.0-draft.6`，检查 `conditional_pass`，待维护者逐页批准 |
| 工程规格准备 | `in_progress`，差异、候选数据模型、接口、错误码、字段映射和既有引用扫描已完成；正式迁移与 OpenAPI 尚未建立 |
| YouYu 正式业务实现 | `blocked` |
| YouYu 正式业务验证 | `not_started` |
| Context 模板成熟度 | `candidate` |
| Harness 里程碑 B | 尚未正式开始 |
| Framework 仓库可见性 | Public，待维护者手动切换 Private |

## 2. A1 与 A2 进度

### A1：规范、候选模板与 Framework 自应用

状态：`completed`

已完成四级 Context、独立回写层、事实源与状态、装配与冲突、完整性检查、五类候选模板和 Framework 自应用。历史自应用评分为 93/100，但不代表候选模板已经通过正式业务项目验证。

### A2：正式业务参考工程验证准备

状态：`active`

已完成：

- YouYu 产品工程目录、项目 Context、工程设计和治理入口；
- 唯一正式 iOS 工程确认及 mPaaS 放弃决策；
- iOS 真机构建、安装和启动，服务地址构建配置注入；
- 服务端构建、App/Gateway 基础接口、内部身份短时签名和单元测试；
- 采集工程依赖修复和构建；
- 既有服务端、采集工程和 iOS 远程重复检查证据；
- 首个业务切片、产品范围、业务规则、验收断言、用户流程、信息架构、页面清单和交互说明；
- YouYu 数据库基础规范采用及 Framework 候选规范登记；
- HTML 高保真候选 `v0.1.0-draft.6` 和 `conditional_pass` 候选检查；
- 登录协议确认两种候选状态和轻量原型检查；
- 当前用户名密码、独立注册、`Long` 主键、旧基础字段、账号资料混表、手机号普通明文字段和 `Map` 响应的工程差异基线；
- App 用户账号、个人资料、短信验证码和协议确认候选数据模型；
- 发送验证码、统一短信登录、退出、当前用户、资料修改、账号信息、协议和地区候选接口；
- 候选错误码以及数据库、Java、OpenAPI、Swift 字段映射；
- YouYu TASK-009 工程规格基线任务启动。
- `sys_user`、`BaseEntity`、登录 ID、Controller、Service、Mapper 和 SQL 的既有引用扫描；扫描确认 App 用户账号必须与管理员 `sys_user` 隔离，字符串登录 ID 不能直接沿用现有 `Long` 身份上下文。

尚未完成：

- 维护者逐页批准 `v0.1.0-draft.6`；
- 候选原型远程成功证据按维护者决定暂缓，恢复 GitHub Actions 服务后重跑；
- 验证码、Token、手机号范围、用户编号、账号状态、资料字段、头像、地区和协议版本关键参数确认；
- 正式数据库迁移、回滚、触发器和实体定义；
- 正式 OpenAPI YAML、示例数据和契约自动检查；
- iOS、服务端和数据库实现任务边界与依赖顺序；
- Git 历史安全问题、共享会话、下游网络隔离、采集待审链路和 iOS 真机体验阻塞关闭；
- 受控业务实现、静态验证、运行验证和模拟用户验收；
- Context 成本、人工修正、遗漏和任务成本复盘；
- 模板成熟度升级判断和里程碑 A 人工退出批准。

## 3. 项目身份与边界

- **仓库**：`zhidao-studio/ai-product-engineering-framework`；
- **定位**：由 zhidao-studio 专有维护、跨平台、可验证的 AI 产品工程框架；
- **默认分支**：`main`；
- **稳定版本边界**：本轮只同步 v0.2.0 未发布开发进度，不修改 `VERSION`，不发布 v0.1.7；
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

## 5. 当前任务

| 任务 | 状态 | 入口 |
|---|---|---|
| 发布 v0.1.6 并同步工程修复与业务准备 | `completed` | [TASK-20260714-010](任务/TASK-20260714-010_发布v0.1.6并同步YouYu工程修复与业务准备.md) |
| 同步 YouYu 产品体验与高保真候选进度 | `completed` | [TASK-20260715-011](任务/TASK-20260715-011_同步YouYu产品体验与高保真候选进度.md) |
| 同步 YouYu 候选原型远程检查阻塞 | `completed` | [TASK-20260715-012](任务/TASK-20260715-012_同步YouYu候选原型远程检查阻塞.md) |
| 记录候选原型远程检查暂缓处理 | `completed` | [TASK-20260715-013](任务/TASK-20260715-013_记录候选原型远程检查暂缓处理.md) |
| 同步 YouYu 高保真 draft.6 与检查拆分 | `completed` | [TASK-20260715-014](任务/TASK-20260715-014_同步YouYu高保真draft.6与检查拆分.md) |
| 同步 YouYu 工程规格基线启动 | `completed` | [TASK-20260715-015](任务/TASK-20260715-015_同步YouYu工程规格基线启动.md) |
| 同步 YouYu 既有引用扫描完成 | `completed` | [TASK-20260715-016](任务/TASK-20260715-016_同步YouYu既有引用扫描完成.md) |
| YouYu TASK-008 高保真人工确认 | `in_review` | YouYu 仓库 `05_项目Context/任务/TASK-008_建设账号与个人中心高保真候选原型.md` |
| YouYu TASK-009 工程规格基线 | `in_progress` | YouYu 仓库 `05_项目Context/任务/TASK-009_建立账号与个人资料工程规格基线.md` |
| 关闭 YouYu 工程基础 P0 阻塞 | `blocked` | YouYu 仓库 `05_项目Context/任务/TASK-004_关闭工程基础P0阻塞.md` |
| 正式业务实现任务 | `not_created` | 高保真、工程规格和阻塞条件满足后创建 |

## 6. 风险与阻塞

| 风险或事项 | 是否阻塞 | 当前处理 | 下一决策点 |
|---|---|---|---|
| Framework 仓库仍为 Public | 阻塞真正访问控制 | 已有专有许可，待维护者切换 Private | 立即执行 |
| 高保真尚未人工批准 | 阻塞客户端实现依据 | `draft.6` 已达人工评审条件 | 维护者逐页确认后 |
| 候选原型远程检查被外部服务阻塞 | 不阻塞人工评审，阻塞自动证据闭环 | 维护者决定暂缓恢复与重跑 | 维护者重新排期后 |
| 工程规格仅为候选 | 阻塞正式联合实现 | 差异、数据模型、接口、错误码、映射和既有引用扫描已完成；正式迁移和 OpenAPI 未完成 | 关键参数确认后 |
| Git 历史安全问题 | 阻塞安全结论 | 轮换凭据、清理历史并建立扫描检查关卡 | SECURITY-001 关闭后 |
| 共享会话与下游网络隔离未验证 | 阻塞正式业务实现 | 已有身份签名单元测试，继续运行验证 | 专项安全任务完成后 |
| 采集待审入库控制缺失 | 阻塞真实采集链路 | 建立候选、审核、正式数据隔离运行证据 | 专项采集任务完成后 |
| iOS 视觉与环境验证未完成 | 阻塞用户体验结论 | 工程可构建，待真机截图和异常验收 | TASK-006 完成后 |
| 正式业务验证尚未开始 | 阻塞模板成熟度升级 | 保持 `candidate` | 里程碑 A 退出前 |

## 7. 下一步

```text
维护者批准高保真并确认关键业务与安全参数
→ 将候选数据模型转为正式迁移、回滚和触发器设计并执行 DB-CHECK
→ 将候选接口、错误码和字段映射转为正式 OpenAPI YAML、示例和契约检查
→ 明确 iOS、服务端和数据库实现边界、依赖顺序和三层验证
→ 并行关闭或形成可审计隔离结论：安全、共享会话、网络隔离、采集待审和 iOS 真机体验
→ 创建受控正式业务实现任务并完成静态、运行和模拟用户三层验证
→ 记录成本、遗漏、冲突和人工修正
→ 回写 Framework，判断候选资产成熟度和里程碑 A 是否退出
```

在高保真批准、工程规格完成和正式实现阻塞具备证据前，不启动正式业务代码实现，不提前宣布进入 Harness B，也不升级候选模板或数据库规范成熟度。

## 8. 更新记录

| 日期 | 变化 | 关联决策或任务 |
|---|---|---|
| 2026-07-12 | 建立 Framework 自身项目 Context Pack 并完成治理修订 | DEC-007 至 DEC-010 / TASK-001 至 TASK-007 |
| 2026-07-13 | YouYu 进入工程基础复核 | TASK-20260713-008 |
| 2026-07-14 | YouYu 工程修复和远程检查完成，进入业务功能准备 | TASK-20260714-009 / TASK-20260714-010 / v0.1.6 |
| 2026-07-15 | YouYu 产品和体验完成，高保真 `draft.5` 进入人工确认 | TASK-20260715-011 |
| 2026-07-15 | 候选原型远程检查被外部服务阻塞并按维护者决定暂缓 | TASK-20260715-012 / TASK-20260715-013 |
| 2026-07-15 | YouYu 高保真更新为 `draft.6`，协议双状态和轻量检查拆分完成同步 | TASK-20260715-014 |
| 2026-07-15 | YouYu 启动 TASK-009，工程差异、候选数据模型、接口、错误码和字段映射完成同步 | TASK-20260715-015 |
| 2026-07-15 | YouYu 完成既有引用扫描，明确 App 用户账号与管理员身份隔离及字符串登录 ID 改造范围 | TASK-20260715-016 |
