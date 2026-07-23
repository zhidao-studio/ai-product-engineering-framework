# 变更记录

本文件记录 AI 产品工程框架的重要版本变化。当前运行状态以 [Framework 项目 Context](12_框架项目Context/README.md) 为准。

## [未发布：0.2.0]

目标：将 Context 与 Harness 从框架定义转化为可执行、可验证的工程能力。

### Context 可执行化

- 建立框架级、项目级、阶段级和任务级 Context；
- 建立事实源、装配、冲突、裁剪和回写规范；
- 建立候选模板和 Framework 自应用；
- 使用 YouYu 真实参考工程验证 Context 能否支撑受控实现和证据回写。
- YouYu 账号与“我”完成本地运行、模拟器严格路径、真机维护者验收和 PR #3 合并；
- 项目 Context、任务 Context 与数据库基础规范提升为 `single_project_validated`；
- 阶段 Context 漂移被记录为 A2 退出前必须修复的问题。
- 记录 YouYu Context 维护成本、至少 8 个明确修正事件和不可测量项；
- 阶段 Context 增加来源提交、最近确认、替代关系、复核触发和过期条件；
- CTX-CHECK-002 完成 YouYu 当前阶段防漂移复验，真实阶段转换仍待验证；
- 维护者于 2026-07-23 批准里程碑 A 退出，A2 标记完成并归档；
- Harness B 保持 `not_started`，不因 A 完成自动启动；

### 当前开发边界

- YouYu 账号与“我”核心路径为 `passed_core_path_by_maintainer`，不等于生产或全部专项通过；
- Context 模板族整体保持 `candidate`，仅项目与任务模板获得单项目证据；
- 数据库基础规范为 `single_project_validated`；
- Harness B 保持 `not_started`；
- 未完成能力不得重复描述为 v0.2.0 已稳定交付。

## [0.1.10] - 2026-07-16

版本定位：Framework 提交可追溯性、发布一致性检查和 YouYu v0.1.4 并发发送修订同步版本。

### Framework 事实源与发布检查

- 修正项目 Context 和 TASK-020 中不可解析的基线 SHA；
- 区分 Framework `source_commit` 与 YouYu `reference_source_commit`；
- 发布脚本从 Framework 项目 Context 读取动态状态，不再硬编码 YouYu 版本、里程碑和成熟度；
- 使用 `git cat-file -e` 校验 Framework 基线与来源提交；
- 支持通过 `YOUYU_REPO_DIR` 校验 YouYu SHA 仓库归属与 VERSION；
- Harness B 状态检查限定在 Roadmap 里程碑 B 段落；
- CHANGELOG 当前版本日期由脚本从版本段解析；
- AGENTS 继续只维护长期规则。

### YouYu v0.1.4 同步

- 同步 Redis Lua 原子发送频控与发送幂等键；
- 同步 Redis 故障失败关闭、供应商失败补偿和防重复发送边界；
- 同步非法 `failed_count` 失败关闭；
- 同步 App 基础数据源、启动期配置校验、严格 Bearer 和 Trace 响应头；
- 同步 OpenAPI v0.1.4、错误码、字段映射和 SERVER-CHECK-004；
- 同步动态测试命名空间、并发发送、Redis 计数和幂等验证定义；
- YouYu 服务端保持 `implemented_not_runtime_validated`；
- YouYu 静态复核保持 `conditional_pass`，运行验证继续 `blocked_external_runtime_evidence`。

### 不提升项

- YouYu Maven、MySQL、Redis、接口和 GitHub Actions 成功证据尚未形成；
- 网络来源频控、完整短信 Outbox、Redis 故障验证和真实短信尚未完成；
- 高保真未批准，iOS 正式实现未开始；
- YouYu 正式业务验证保持 `not_started`；
- Context 模板和数据库规范保持 `candidate`；
- Harness B 保持 `not_started`；
- 核心模型和许可模式未改变。

报告：[v0.1.10 YouYu并发发送与事实源修订同步报告](10_版本演进/v0.1.10YouYu并发发送与事实源修订同步报告.md)。

## [0.1.9] - 2026-07-16

> 历史快照：记录 YouYu v0.1.3 静态修订和 Framework 动态事实源治理，当前由 v0.1.10 与项目 Context 替代。

- 同步 v0.1.3 数据库审计、验证码消费行锁、配置、契约和初版等价检查脚本；
- AGENTS 删除动态状态，新增初版发布一致性脚本；
- 后续复核发现发送频控并发和 Context SHA 问题，由 v0.1.10 修订；
- 未取得运行验证证据。

## [0.1.8] - 2026-07-16

> 历史快照：记录 YouYu v0.1.2 当时状态，当前由后续版本和项目 Context 替代。

- 同步初步静态修复、测试和联合工作流；
- 候选资产成熟度未提升，Harness B 未启动。

## [0.1.7] - 2026-07-16

> 历史快照：记录 YouYu v0.1.1 服务端基础实现，当前由后续版本替代。

- 同步参数、数据库、OpenAPI 和服务端基础实现；
- 正式业务验证保持 `not_started`。

## [0.1.6] - 2026-07-14

> 历史快照：当前状态以 Framework 项目 Context 为准。

- 同步 YouYu 工程修复和业务准备；
- Context 模板保持 `candidate`，Harness B 未启动。

## [0.1.5] - 2026-07-12

- 收敛当前状态入口和历史边界。

## [0.1.4] - 2026-07-12

- 统一中文术语和表达。

## [0.1.3] - 2026-07-12

- 同步早期工程证据并建立历史验证记录。

## [0.1.2] - 2026-07-12

- 采用 Proprietary / All Rights Reserved。

## [0.1.1] - 2026-07-12

- 完成全仓复核、事实源清理和版本治理。

## [0.1.0] - 2026-07-12

- 建立愿景、三平面、十阶段、五大基础设施、角色和参考工程入口。
