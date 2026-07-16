# AI 产品工程框架：项目 Context Pack

> 本文件是 Framework 当前版本、里程碑、工作段、参考工程状态、阻塞和下一步的唯一入口。README、Roadmap、AGENTS、历史任务、验证和发布报告不得覆盖本文件。

```yaml
project_context_id: PROJ-CONTEXT-AIPEF
project: AI Product Engineering Framework
status: active
execution_status: active
project_context_pack_version: 0.2-A.23
owner: zhidao-studio
current_stage: 质量与安全验证
current_work_segment: A2 / YouYu 运行验证
stable_release: v0.1.9
target_release: v0.2.0
current_milestone: A / Context 可执行化
working_branch: main
baseline_commit: 651c87e28bf38b07a02d36ff1b93550f802cda70
source_commit: 59c42addf58f4cfc69b8d33e06015d2cd3e11c4e
youyu_release: v0.1.3
youyu_source_commit: f881c219c6ebeb869a9fcb6eaa4b322dffe1e907
youyu_server_implementation_status: implemented_not_runtime_validated
youyu_static_review_status: passed
youyu_runtime_validation_status: blocked_external_runtime_evidence
youyu_formal_business_validation: not_started
youyu_high_fidelity_status: draft_for_confirmation
youyu_ios_business_implementation_status: not_started
youyu_network_rate_limit_status: not_implemented
context_template_maturity: candidate
database_standard_maturity: candidate
harness_milestone_b: not_started
framework_sync_task: TASK-20260716-020
license_model: proprietary_all_rights_reserved
last_verified_at: 2026-07-16
sensitivity: proprietary
```

## 1. 当前结论

| 项目 | 当前事实 |
|---|---|
| 稳定版本 | `v0.1.9` |
| 目标版本 | `v0.2.0` |
| 当前里程碑 | A / Context 可执行化 |
| 当前工作段 | A2 / YouYu 运行验证 |
| YouYu 版本 | `v0.1.3` |
| YouYu 服务端 | `implemented_not_runtime_validated` |
| YouYu 静态复核 | `passed` |
| YouYu 运行验证 | `blocked_external_runtime_evidence` |
| YouYu 正式业务验证 | `not_started` |
| YouYu 高保真 | `draft_for_confirmation` |
| YouYu iOS 正式实现 | `not_started` |
| Context 模板 | `candidate` |
| 数据库规范 | `candidate` |
| Harness B | `not_started` |

v0.1.9 是事实源收敛和参考工程静态修订同步版本，不代表 YouYu 运行验证完成，也不代表 v0.2.0 里程碑 A 已退出。

## 2. A1 与 A2

### A1：规范、候选模板与 Framework 自应用

状态：`completed`

四级 Context、事实源、装配与冲突、独立回写层、完整性检查、候选模板和 Framework 自应用已经完成。该结果不替代真实业务项目验证。

### A2：正式业务参考工程验证

状态：`active`

当前子步骤：**YouYu v0.1.3 运行验证**。

已完成：

- YouYu 产品规则、体验和高保真候选；
- App 账号域与管理员账号域隔离；
- 数据库规范、关键参数和服务端先行例外；
- 四张账号域表、迁移、回滚、OpenAPI 和服务端实现；
- v0.1.3 数据库审计触发器和创建时间保护；
- 验证码数据库行锁、并发失败次数和单次消费修订；
- App/Admin 显式数据库配置、H2 测试范围、SQL 参数日志和 Gateway 地址修订；
- 协议数组、去空白后的 Unicode 码点、Trace ID 和短信适配边界修订；
- YouYu Project Context Pack、TASK-011、TASK-012 和 SERVER-CHECK-003；
- 本地等价检查脚本和调用该脚本的 Actions；
- Framework AGENTS 与版本规范动态状态收敛；
- Framework 发布状态一致性脚本。

尚未完成：

- YouYu Maven 测试和打包实际成功；
- MySQL 迁移、审计行为、约束和回滚实际成功；
- Gateway、App、MySQL 和 Redis 联合运行；
- Redis 停机、网络分区和配置不一致验证；
- 并发验证码和日志安全实际结果；
- 网络来源频控；
- 真实短信供应商；
- 高保真逐页批准；
- iOS、Keychain、真机和模拟用户验收；
- 失败、成本、人工修正和 Framework 改进回写；
- 里程碑 A 人工退出批准。

## 3. v0.1.9 关键治理修订

```text
长期规则 → AGENTS
动态状态 → Framework项目Context
版本历史 → CHANGELOG与Roadmap
参考工程事实 → 参考工程入口与YouYu Context
```

- AGENTS 不再维护当前版本、工作段、YouYu 版本、任务和检查结果；
- 当前稳定版本只从 `VERSION` 读取；
- `scripts/check-release-state.sh` 检查 VERSION、README、CHANGELOG、Roadmap、Context、AGENTS 与 YouYu 参考状态；
- 历史任务、验证和报告保留原结论，并增加历史快照和替代关系；
- 检查定义不等于运行通过；
- 候选资产不因版本发布自动提升成熟度。

## 4. 当前权威入口

| 主题 | 权威来源 |
|---|---|
| 许可 | [LICENSE](../LICENSE) |
| 框架定义 | [愿景与定位](../01_框架定义/AI产品工程框架愿景与定位.md) |
| Context 工程 | [Context 工程](../04_Context工程/README.md) |
| Harness | [执行控制与检查关卡](../05_Harness工程/执行控制与检查关卡.md) |
| 数据库候选规范 | [数据库设计基础规范](../08_模板资产/工程规格/数据库设计基础规范.md) |
| 当前参考工程 | [参考工程入口](../09_参考工程/README.md) |
| 当前阶段 | [v0.2-A 阶段 Context](阶段/v0.2-A_Context可执行化.md) |
| 版本路线 | [Roadmap](../10_版本演进/Roadmap.md) |
| v0.1.9 报告 | [YouYu静态正确性修订同步报告](../10_版本演进/v0.1.9YouYu静态正确性修订同步报告.md) |

## 5. 当前任务

| 任务 | 状态 |
|---|---|
| [TASK-20260716-020](任务/TASK-20260716-020_同步YouYuv0.1.3静态修订.md) | `completed` |
| YouYu TASK-011 服务端运行验证 | `blocked_external_runtime_evidence` |
| YouYu TASK-012 网络来源频控 | `not_started` |
| YouYu 高保真人工确认 | `in_review` |
| YouYu iOS 正式实现 | `not_started` |

## 6. 当前阻塞

| 阻塞 | 当前处理 |
|---|---|
| YouYu 缺少 Maven/MySQL/Redis/接口证据 | 在等价环境运行本地检查脚本并回写 |
| Redis 故障未验证 | 独立安全环境执行，不从待办删除 |
| 网络来源频控未实现 | YouYu TASK-012 |
| 真实短信未接入 | 保持生产失败关闭，后续独立任务 |
| 高保真未批准、iOS 未开始 | 不形成体验和端到端结论 |
| 历史安全与网络隔离 | 继续专项证据收集 |

## 7. 下一步

```text
运行YouYu scripts/check-account-slice.sh
→ 保存Maven/MySQL/Redis/接口证据
→ 修复运行问题并完成TASK-011
→ 完成Redis故障验证与TASK-012
→ 高保真人工批准
→ 单独创建iOS正式实现任务
→ 真机和模拟用户验收
→ 回写Framework并评估A2退出
```

在真实运行证据完成前，YouYu 正式业务验证保持 `not_started`，Context 模板和数据库规范保持 `candidate`，Harness B 保持 `not_started`。
