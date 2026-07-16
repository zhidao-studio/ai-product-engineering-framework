# 参考工程

> 参考工程用于证明 Framework 能够控制真实产品交付，而不是只形成文档。当前状态以 [Framework 项目 Context](../12_框架项目Context/README.md) 为准。

## 1. 参考工程必须覆盖

- 价值与产品范围；
- 用户流程与高保真；
- 工程架构、API 和数据约定；
- 项目、阶段和任务 Context；
- 受控实现任务；
- 静态、数据库、运行、安全和模拟用户验证；
- 发布或可运行交付；
- 用户反馈或代理指标；
- 对 Framework 的反向改进。

## 2. 当前参考工程：YouYu

```text
YouYu版本：v0.1.3
当前里程碑：A / Context 可执行化
当前工作段：A2 / YouYu运行验证
首个业务切片：手机号验证码登录注册与个人资料管理
产品规则：confirmed
体验定义：confirmed
高保真：v0.1.0-draft.6 / draft_for_confirmation
数据库迁移：implemented_not_executed
OpenAPI：implemented_for_v0.1.3
服务端实现：implemented_not_runtime_validated
静态复核：passed
运行验证：blocked_external_runtime_evidence
网络来源频控：not_implemented
iOS正式实现：not_started
正式业务验证：not_started
Context模板成熟度：candidate
数据库规范成熟度：candidate
Harness里程碑B：not_started
```

## 3. 当前追溯链

```text
产品规则与体验定义
→ 高保真候选
→ 工程规格与旧实现扫描
→ 参数确认与受控例外
→ 数据库和OpenAPI
→ 服务端实现
→ v0.1.2初步验证加固
→ v0.1.3审计、并发、配置和契约静态修订
→ 本地等价验证脚本与SERVER-CHECK-003
→ TASK-011等待运行证据
```

## 4. v0.1.3 已形成事实

- App 普通用户与管理员 `sys_user` 保持隔离；
- 四张账号域表、历史建表迁移和 v0.1.3 审计触发器修订已建立；
- 插入审计时间不可由调用方指定，更新时创建时间受保护；
- 数据库检查逐项验证主键、唯一索引和触发器正文；
- 验证码通过数据库行锁收口失败次数与单次消费；
- App/Admin Profile、数据库默认值和 SQL 参数输出已收敛；
- Gateway 下游地址环境化；
- 协议数组、Unicode 字符长度、Trace ID 和短信适配边界与 OpenAPI 对齐；
- YouYu Project Context Pack、TASK-011、TASK-012 和 SERVER-CHECK-003 已建立；
- GitHub Actions 与本地统一调用 `scripts/check-account-slice.sh`。

## 5. 检查定义与执行证据

```text
代码已实现
≠ 静态复核通过
≠ 运行检查已执行通过
```

当前只有静态复核结论 `passed`。未取得：

- Maven 测试与打包成功日志；
- MySQL 迁移、行为和回滚成功日志；
- Redis 跨进程共享会话证据；
- Gateway/App 端到端证据；
- Redis 故障验证；
- 并发验证码实际请求结果；
- 日志安全实际运行结果。

因此不能将 YouYu 标记为 `single_project_validated`。

## 6. 当前明确缺口

- 网络来源频控，YouYu TASK-012 `not_started`；
- 真实短信供应商；
- 高保真逐页批准；
- iOS 正式业务实现与 Keychain；
- 真机和模拟用户验收；
- 历史安全、网络隔离和采集待审链路证据；
- 失败、成本、人工修正和 Framework 改进回写。

## 7. 正式参考工程通过标准

只有下列证据完整，才能评估 `single_project_validated`：

1. 产品、体验和工程事实可追溯且人工批准；
2. Context 可由新 Agent 独立恢复；
3. 修改边界、接口和检查关卡真实生效；
4. 静态、数据库、运行、安全和模拟用户验证完成；
5. iOS 与服务端完成真实端到端路径；
6. 失败、人工修正、成本和遗漏有记录；
7. 运行结果和 Framework 改进完成回写；
8. 人类责任人批准最终结论。

当前正式业务验证保持 `not_started`，Context 模板与数据库规范保持 `candidate`，Harness B 保持 `not_started`。

## 8. 下一步

```text
在等价环境运行YouYu scripts/check-account-slice.sh
→ 回写Maven/MySQL/Redis/接口证据
→ 修复运行问题并完成TASK-011
→ 完成Redis故障验证与TASK-012
→ 高保真人工批准
→ 单独创建iOS正式实现任务
→ 真机与模拟用户验收
→ 回写Framework成熟度评估
```

历史首轮复核保留在 REF-CHECK-001，其早期结论不代表当前参考工程通过。
