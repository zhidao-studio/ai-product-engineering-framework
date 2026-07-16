# AI 产品工程框架：项目 Context Pack

> 本文件是 Framework 当前版本、工作段、参考工程状态、阻塞和下一步的唯一动态入口。README、Roadmap、AGENTS、历史任务、验证和发布报告不得覆盖本文件。

```yaml
project_context_id: PROJ-CONTEXT-AIPEF
project: AI Product Engineering Framework
status: active
execution_status: paused
project_context_pack_version: 0.2-A.25
owner: zhidao-studio
current_stage: 参考工程运行开发
current_work_segment: A2 / 冻结Framework并本地跑通YouYu
current_action: freeze_framework_and_run_reference_project
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
youyu_runtime_validation_status: pending_local_macos_execution
youyu_formal_business_validation: not_started
youyu_high_fidelity_status: draft_for_confirmation
youyu_ios_business_implementation_status: not_started
youyu_local_ci_platform: local_macos_homebrew
youyu_local_ci_status: defined_not_executed
framework_sync_status: frozen
framework_change_policy: frozen_until_youyu_core_path_runtime_passed
context_template_maturity: candidate
database_standard_maturity: candidate
harness_milestone_b: not_started
license_model: proprietary_all_rights_reserved
last_verified_at: 2026-07-17
sensitivity: proprietary
```

## 1. 当前结论

Framework 保持 `v0.1.10`，不发布 `v0.1.11`，不新增同步报告，不修改 Roadmap，不新建 Framework 同步任务。

当前唯一主动作是：

```text
冻结 Framework
→ 在本地 macOS 编译和启动 YouYu v0.1.4
→ 只修阻止首个账号业务路径运行的问题
→ 取得真实运行日志
→ 登录注册与“我”核心路径跑通后再回写 Framework
```

当前没有新的 Maven、MySQL、Redis、App、Gateway、接口或 iOS 成功证据。Framework 文档数量和修订版本不构成参考工程通过证据。

## 2. 为什么冻结 Framework

YouYu 当前不是缺少更多静态 Review，而是尚未进入完整运行开发：

- Maven 测试和打包没有实际成功证据；
- MySQL 迁移和结构检查没有实际执行证据；
- Redis Lua 没有实际执行证据；
- App 与 Gateway 没有联合启动证据；
- 登录、个人资料和退出没有端到端结果；
- 本地自动脚本仍为 `defined_not_executed`。

此前形成了以下低效循环：

```text
静态Review
→ 发现更多生产级问题
→ 修改代码与文档
→ 同步Framework版本
→ 没有实际启动环境
→ 无法证明可运行
→ 再次静态Review
```

Framework 已从“帮助参考工程交付”逐渐变成“同步成本”。在 YouYu 核心路径跑通前，继续沉淀候选规范会扩大这一问题。

## 3. 当前交付阶段重新分层

### 阶段一：本地开发完成

本阶段只要求：

- 服务可以编译和启动；
- MySQL 和 Redis 可以连接；
- 可以发送模拟验证码；
- 新手机号可以注册登录；
- 可以查询当前用户和账号；
- 可以修改昵称与简介；
- 可以退出，旧 Token 不再可用。

### 阶段二：工程验证完成

后续再完成：

- 单元测试；
- MySQL 行为和回滚测试；
- Redis 与并发测试；
- 配置和日志测试；
- 自动化重复执行。

### 阶段三：生产安全完成

不阻塞当前本地闭环：

- 真实短信供应商；
- 完整短信 Outbox；
- 网络来源频控；
- Redis 网络分区与 Cluster 优化；
- Token 与数据库最终一致性重构；
- 灰度、监控和完整生产日志审计。

## 4. 当前版本 P0 定义

只有以下问题可以阻塞 YouYu 首个业务切片：

1. 编译失败；
2. 服务无法启动；
3. 数据库迁移失败；
4. Redis 无法连接；
5. 模拟验证码无法发送；
6. 注册或登录失败；
7. `/users/me` 或账号查询失败；
8. 昵称和简介修改失败；
9. 退出失败或旧 Token 仍可访问；
10. 明确的数据安全漏洞。

其他发现进入 backlog，不再触发 Framework 版本、报告、Roadmap 或任务同步。

## 5. 本地执行顺序

```text
准备 Homebrew、JDK 21、Maven、MySQL、Redis
→ 使用固定 youyu 数据库执行 v0.1.1 与 v0.1.3 SQL
→ 注入本地开发环境变量
→ mvn clean test
→ mvn package
→ 启动 youyu-app
→ 启动 youyu-gateway
→ 按核心接口路径执行 curl
→ 从第一个真实错误开始修复
```

核心接口路径：

```text
查询当前协议
→ 发送模拟验证码
→ 使用 123456 注册登录
→ 获取 Token
→ 查询 /users/me
→ 查询 /users/me/account
→ 修改昵称和简介
→ 再次查询 /users/me
→ 退出
→ 验证旧 Token 失效
```

到上述路径实际成功并保存日志后，才可以声明首个账号登录注册与“我”模块跑通。

## 6. Framework 冻结规则

在 YouYu 核心路径真实跑通前：

- 不升级 Framework 版本；
- 不新增 Framework 同步报告；
- 不修改 Roadmap；
- 不新建 Framework 同步任务；
- 不提升 Context、数据库规范或 Harness 资产成熟度；
- 不把新的 YouYu 静态问题立即抽象成 Framework 规范；
- 不用 Framework 自应用代替参考工程运行证据。

允许的唯一 Framework 变更是修复会直接阻止读取当前状态的严重事实错误。

## 7. Framework 解冻条件

必须同时满足：

1. YouYu v0.1.4 在本地 macOS 完成 Maven 构建；
2. MySQL 迁移执行成功；
3. Redis、App 和 Gateway 联合启动成功；
4. 账号核心接口路径完整成功；
5. 真实命令、错误、修复和日志位置已记录；
6. 项目维护者确认首个业务路径可操作。

解冻后只做一次经验回写，优先萃取“本地运行开发优先、完成标准分层、Review 终止条件和 Framework 同步节奏”，而不是逐问题同步版本。

## 8. 当前状态边界

- Framework 稳定版本保持 `v0.1.10`；
- YouYu 稳定版本保持 `v0.1.4`；
- YouYu 服务端仍为 `implemented_not_runtime_validated`；
- YouYu 本地 CI 仍为 `defined_not_executed`；
- 正式业务验证保持 `not_started`；
- Context 模板和数据库规范保持 `candidate`；
- Harness B 保持 `not_started`。

下一轮输入必须是本地 macOS 的编译、启动或接口日志，不再以仓库新增了多少文档作为进展依据。