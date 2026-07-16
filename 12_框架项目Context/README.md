# AI 产品工程框架：项目 Context Pack

> 本文件是 Framework 当前版本、里程碑、工作段、参考工程状态、阻塞和下一步的唯一入口。README、Roadmap、AGENTS、历史任务、验证和发布报告不得覆盖本文件。

```yaml
project_context_id: PROJ-CONTEXT-AIPEF
project: AI Product Engineering Framework
status: active
execution_status: active
project_context_pack_version: 0.2-A.24
owner: zhidao-studio
current_stage: 质量与安全验证
current_work_segment: A2 / YouYu 运行验证
stable_release: v0.1.10
target_release: v0.2.0
current_milestone: A / Context 可执行化
working_branch: main
baseline_commit: 651c87e2bf4a86757af4682c4348a83470b80934
source_commit: 50c4c9328a89ad0950c3bc266b630a7ebc9db5ae
youyu_release: v0.1.4
youyu_source_commit: c1f7763323cc7b6fe2086247be2d901700265339
youyu_server_implementation_status: implemented_not_runtime_validated
youyu_static_review_status: conditional_pass
youyu_runtime_validation_status: blocked_external_runtime_evidence
youyu_formal_business_validation: not_started
youyu_high_fidelity_status: draft_for_confirmation
youyu_ios_business_implementation_status: not_started
youyu_sms_send_atomic_rate_limit_status: implemented_not_runtime_validated
youyu_network_rate_limit_status: not_implemented
youyu_sms_outbox_status: not_implemented
context_template_maturity: candidate
database_standard_maturity: candidate
harness_milestone_b: not_started
framework_sync_task: TASK-20260716-021
license_model: proprietary_all_rights_reserved
last_verified_at: 2026-07-16
sensitivity: proprietary
```

## 1. 当前结论

| 项目 | 当前事实 |
|---|---|
| 稳定版本 | `v0.1.10` |
| 目标版本 | `v0.2.0` |
| 当前里程碑 | A / Context 可执行化 |
| 当前工作段 | A2 / YouYu 运行验证 |
| YouYu 版本 | `v0.1.4` |
| YouYu 服务端 | `implemented_not_runtime_validated` |
| YouYu 静态复核 | `conditional_pass` |
| YouYu 运行验证 | `blocked_external_runtime_evidence` |
| YouYu 正式业务验证 | `not_started` |
| YouYu 高保真 | `draft_for_confirmation` |
| YouYu iOS 正式实现 | `not_started` |
| Context 模板 | `candidate` |
| 数据库规范 | `candidate` |
| Harness B | `not_started` |

v0.1.10 是 Framework 提交可追溯性、发布一致性检查和 YouYu v0.1.4 静态修订同步版本，不代表 YouYu 运行验证完成，也不代表里程碑 A 已退出。

## 2. 当前 A2 事实

### 已完成

- YouYu 产品规则、体验定义和高保真候选；
- App 账号域与管理员账号域隔离；
- 四张账号域表、数据库规范和 v0.1.3 审计触发器修订；
- 验证码消费数据库行锁、失败次数和单次消费；
- v0.1.4 Redis Lua 原子发送门禁、幂等键和 Redis 失败关闭；
- App 基础数据源、启动期配置校验、严格 Bearer 和 Trace 响应头；
- OpenAPI v0.1.4、错误码、字段映射和 SERVER-CHECK-004；
- 可重复本地检查脚本与调用相同脚本的 Actions；
- Framework 无效基线修正、跨仓库 SHA 字段区分和发布脚本动态解析；
- TASK-20260716-021 和 v0.1.10 同步报告。

### 尚未完成

- YouYu Maven 测试和打包实际成功；
- MySQL 迁移、审计行为、约束和回滚实际成功；
- Redis Lua 并发发送、幂等和计数实际结果；
- Gateway、App、MySQL 和 Redis 联合运行；
- Redis 停机、网络分区和配置不一致验证；
- 完整短信 Outbox、Token/数据库一致性验证和网络来源频控；
- 真实短信供应商；
- 高保真逐页批准；
- iOS、Keychain、真机和模拟用户验收；
- 失败、成本、人工修正和 Framework 改进回写；
- 里程碑 A 人工退出批准。

## 3. v0.1.10 治理修订

```text
长期规则 → AGENTS
动态状态 → Framework项目Context
稳定版本 → VERSION与CHANGELOG
参考工程事实 → YouYu Context与Framework reference字段
提交归属 → Framework source_commit / YouYu reference_source_commit
```

- `baseline_commit` 已修正为真实 Framework 提交；
- TASK-020 保留历史结论，但修正提交字段语义并标记由 TASK-021 替代；
- `scripts/check-release-state.sh` 从本 Context 解析动态状态；
- Framework 基线和来源提交通过 `git cat-file -e` 校验；
- 设置 `YOUYU_REPO_DIR` 后可校验 YouYu 提交归属和 VERSION；
- 未提供 YouYu 仓库时只校验 SHA 格式，并明确不宣称仓库归属已验证；
- Harness B 状态只在 Roadmap 里程碑 B 段落检查；
- 检查定义不等于运行通过；
- 候选资产不因修订版本发布自动提升成熟度。

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
| v0.1.10 报告 | [YouYu并发发送与事实源修订同步报告](../10_版本演进/v0.1.10YouYu并发发送与事实源修订同步报告.md) |

## 5. 当前任务

| 任务 | 状态 |
|---|---|
| [TASK-20260716-021](任务/TASK-20260716-021_同步YouYuv0.1.4并发发送修订.md) | `completed` |
| YouYu TASK-011 服务端运行验证 | `blocked_external_runtime_evidence` |
| YouYu TASK-012 网络来源频控 | `not_started` |
| YouYu 完整短信 Outbox | `not_started` |
| YouYu 高保真人工确认 | `in_review` |
| YouYu iOS 正式实现 | `not_started` |

## 6. 当前阻塞

| 阻塞 | 当前处理 |
|---|---|
| YouYu 缺少 Maven/MySQL/Redis/接口证据 | 在等价环境运行本地检查脚本并回写 |
| Redis 故障未验证 | 独立安全环境执行，不从待办删除 |
| Outbox 与网络来源频控未实现 | 建立独立后续任务，不宣称完整短信安全闭环 |
| 真实短信未接入 | 保持生产失败关闭 |
| 高保真未批准、iOS 未开始 | 不形成体验和端到端结论 |

## 7. 下一步

```text
运行YouYu scripts/check-account-slice.sh
→ 保存Maven/MySQL/Redis/并发发送/接口证据
→ 修复运行问题并完成TASK-011
→ 完成Redis故障、Outbox与TASK-012
→ 高保真人工批准
→ 单独创建iOS正式实现任务
→ 真机和模拟用户验收
→ 回写Framework并评估A2退出
```

在真实运行证据完成前，YouYu 正式业务验证保持 `not_started`，Context 模板和数据库规范保持 `candidate`，Harness B 保持 `not_started`。
