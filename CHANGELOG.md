# 变更记录

本文件记录 AI 产品工程框架的重要版本变化。当前运行状态以 [Framework 项目 Context](12_框架项目Context/README.md) 为准。

## [未发布：0.2.0]

目标：将 Context 与 Harness 从框架定义转化为可执行、可验证的工程能力。

### Context 可执行化

- 建立框架级、项目级、阶段级和任务级 Context；
- 建立事实源、装配、冲突、裁剪和回写规范；
- 建立候选模板和 Framework 自应用；
- 使用 YouYu 真实参考工程验证 Context 能否支撑受控实现和证据回写。

### 当前开发边界

- YouYu 仍处于运行验证等待阶段；
- YouYu 正式业务验证保持 `not_started`；
- Context 模板和数据库规范保持 `candidate`；
- Harness B 保持 `not_started`；
- 未完成能力不得重复描述为 v0.2.0 已稳定交付。

## [0.1.9] - 2026-07-16

版本定位：全仓事实源收敛、YouYu v0.1.3 静态正确性修订同步与发布治理修订版本。

### YouYu v0.1.3 同步

- 同步数据库审计触发器修订和创建时间不可篡改规则；
- 同步触发器正文、主键和必要唯一索引逐项断言；
- 同步验证码数据库行锁、失败次数并发安全和单次消费；
- 同步 App/Admin Profile、数据库默认值、SQL 参数日志和 Gateway 地址修订；
- 同步协议数组、Unicode 长度、Trace ID 和短信适配边界；
- 同步 YouYu Project Context Pack、TASK-011、TASK-012 和 SERVER-CHECK-003；
- 同步本地等价检查脚本和调用相同脚本的 Actions；
- YouYu 静态复核为 `passed`，运行验证继续 `blocked_external_runtime_evidence`。

### Framework 治理

- AGENTS 删除动态稳定版本、工作段、YouYu 版本、任务和检查结果；
- 动态状态统一由 Framework 项目 Context 管理；
- 版本规范明确示例不是当前版本，当前稳定版本由 `VERSION` 决定；
- 历史版本表补齐 v0.1.7、v0.1.8、v0.1.9；
- 新增 `scripts/check-release-state.sh`；
- README、Roadmap、阶段 Context 和参考工程统一到 YouYu v0.1.3；
- 历史任务、验证和报告增加快照和替代边界。

### 不提升项

- YouYu Maven、MySQL、Redis、端到端和 GitHub Actions 成功证据尚未形成；
- 网络来源频控、Redis 故障验证和真实短信尚未完成；
- 高保真仍未批准，iOS 正式实现仍未开始；
- YouYu 正式业务验证保持 `not_started`；
- Context 模板和数据库规范保持 `candidate`；
- Harness B 保持 `not_started`；
- 核心模型和许可模式未改变。

报告：[v0.1.9 YouYu静态正确性修订同步报告](10_版本演进/v0.1.9YouYu静态正确性修订同步报告.md)。

## [0.1.8] - 2026-07-16

> 历史快照：记录 YouYu v0.1.2 当时的验证加固状态，当前由 v0.1.9 和 Framework 项目 Context 替代。

- 同步 YouYu v0.1.2 初步静态修复、测试、数据库断言和联合工作流；
- 同步 SERVER-CHECK-002 与 TASK-011 外部运行阻塞；
- 稳定版本更新为 v0.1.8；
- 候选资产成熟度未提升，Harness B 未启动。

报告：[v0.1.8 YouYu验证加固同步报告](10_版本演进/v0.1.8YouYu验证加固同步报告.md)。

## [0.1.7] - 2026-07-16

> 历史快照：记录 YouYu v0.1.1 服务端基础实现，当前由后续版本和项目 Context 替代。

- 同步 YouYu 参数、数据库、OpenAPI 和服务端基础实现；
- 同步字符串身份、Bearer 网关和失败关闭边界；
- 新增 TASK-011；
- 稳定版本更新为 v0.1.7；
- 正式业务验证保持 `not_started`。

## [0.1.6] - 2026-07-14

> 历史快照：当前状态以 Framework 项目 Context 为准。

- 同步 YouYu 工程修复和业务准备；
- 稳定版本更新为 v0.1.6；
- Context 模板保持 `candidate`，Harness B 未启动。

## [0.1.5] - 2026-07-12

- 收敛当前状态入口和历史边界；
- 稳定版本更新为 v0.1.5。

## [0.1.4] - 2026-07-12

- 统一中文术语和表达；
- 稳定版本更新为 v0.1.4。

## [0.1.3] - 2026-07-12

- 同步早期工程证据并建立历史验证记录；
- 稳定版本更新为 v0.1.3。

## [0.1.2] - 2026-07-12

- 采用 Proprietary / All Rights Reserved；
- 稳定版本更新为 v0.1.2。

## [0.1.1] - 2026-07-12

- 完成全仓复核、事实源清理和版本治理；
- 稳定版本更新为 v0.1.1。

## [0.1.0] - 2026-07-12

- 建立愿景、三平面、十阶段、五大基础设施、角色和参考工程入口。
