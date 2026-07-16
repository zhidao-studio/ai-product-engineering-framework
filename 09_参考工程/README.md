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
YouYu版本：v0.1.4
当前里程碑：A / Context 可执行化
当前工作段：A2 / YouYu运行验证
首个业务切片：手机号验证码登录注册与个人资料管理
产品规则：confirmed
体验定义：confirmed
高保真：v0.1.0-draft.6 / draft_for_confirmation
数据库迁移：implemented_not_executed
OpenAPI：implemented_for_v0.1.4
服务端实现：implemented_not_runtime_validated
静态复核：conditional_pass
运行验证：blocked_external_runtime_evidence
手机号与设备原子发送频控：implemented_not_runtime_validated
网络来源频控：not_implemented
完整短信Outbox：not_implemented
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
→ 工程规格与受控例外
→ v0.1.3数据库审计和验证码消费并发修订
→ v0.1.4验证码发送并发、配置与契约修订
→ OpenAPI v0.1.4与SERVER-CHECK-004
→ 本地等价验证脚本
→ TASK-011等待运行证据
```

## 4. v0.1.4 已形成的仓库事实

- App 普通用户与管理员 `sys_user` 保持隔离；
- 四张账号域表、历史建表迁移和 v0.1.3 审计触发器修订继续有效；
- 验证码消费通过数据库行锁收口失败次数与单次消费；
- Redis Lua 原子完成手机号冷却、手机号日限额、设备日限额和幂等预占；
- 相同发送幂等键不会重复进入短信供应商；
- Redis 不可用时失败关闭，不回退 JVM 本地计数；
- 非法 `failed_count` 按主键锁定；
- App 基础数据源覆盖所有 Profile，账号安全参数增加启动校验；
- Gateway 只接受标准 Bearer，Trace ID 在响应提交前写入；
- OpenAPI v0.1.4 成为当前唯一权威契约；
- SERVER-CHECK-003 转为历史快照，当前验证记录为 SERVER-CHECK-004；
- GitHub Actions 与本地统一调用 `scripts/check-account-slice.sh`。

## 5. 检查定义与执行证据

```text
代码已实现
≠ 静态条件通过
≠ 运行检查已执行通过
```

当前静态状态为 `conditional_pass`。尚未取得：

- Maven 测试与打包成功日志；
- MySQL 迁移、行为和回滚成功日志；
- Redis Lua 并发发送、计数和幂等实际结果；
- Redis 跨进程共享会话证据；
- Gateway/App 端到端证据；
- Redis 故障验证；
- 并发验证码实际请求结果；
- 日志安全实际运行结果。

因此不能将 YouYu 标记为 `single_project_validated`。

## 6. 当前明确缺口

- 完整短信 Outbox 与供应商成功后数据库失败恢复；
- Token 签发与数据库提交一致性验证；
- 网络来源频控，YouYu TASK-012 `not_started`；
- 真实短信供应商；
- 高保真逐页批准；
- iOS 正式业务实现与 Keychain；
- 真机和模拟用户验收；
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
→ 回写Maven/MySQL/Redis/并发发送/接口证据
→ 修复运行问题并完成TASK-011
→ 完成Redis故障、Outbox与TASK-012
→ 高保真人工批准
→ 单独创建iOS正式实现任务
→ 真机与模拟用户验收
→ 回写Framework成熟度评估
```

历史首轮复核保留在 REF-CHECK-001，其早期结论不代表当前参考工程通过。
