# 参考工程

> 参考工程用于证明 Framework 能够控制真实产品交付，而不是只形成文档。当前运行状态以 [Framework 项目 Context](../12_框架项目Context/README.md) 为准。

## 1. 参考工程必须覆盖

- 价值与产品范围；
- 用户流程与高保真；
- 工程架构、API 和数据约定；
- 项目、阶段和任务 Context；
- 受控 AI 实现任务；
- 静态、数据库、运行、安全和模拟用户验证；
- 发布或可运行交付；
- 用户反馈或代理指标；
- 对 Framework 的反向改进。

## 2. 当前参考工程：YouYu

```text
YouYu版本：v0.1.2
当前里程碑：A / Context 可执行化
当前工作段：A2 / 运行验证待执行
首个业务切片：手机号验证码登录注册与个人资料管理
产品定义：completed
体验定义：confirmed
高保真：v0.1.0-draft.6 / conditional_pass / 待维护者批准
关键参数：confirmed
数据库迁移与回滚：implemented / not_executed
OpenAPI：implemented_for_v0.1.2
服务端实现：implemented_not_runtime_validated
静态复核：conditional_pass
自动检查：defined / not_executed
iOS正式实现：not_started
正式业务验证：not_started
Context模板成熟度：candidate
数据库规范成熟度：candidate
Harness里程碑B：not_started
```

## 3. 当前追溯链

```text
产品范围与业务规则
→ 用户流程与高保真候选
→ 工程差异和既有引用扫描
→ 关键参数人工确认
→ 数据库迁移、回滚和OpenAPI
→ 服务端受控实现
→ v0.1.2静态缺陷修复
→ 单元测试与数据库断言
→ 账号业务切片联合工作流
→ TASK-011等待运行证据
```

## 4. v0.1.2 已形成事实

### 实现与修复

- App 普通用户与管理员 `sys_user` 保持隔离；
- 四张账号域表、触发器、回滚和数据库规范已经建立；
- 手机号验证码统一登录注册、协议确认、当前用户和资料修改已经实现；
- 字符串 App 身份、旧管理员 Long 身份、Bearer 网关和共享 Redis 配置已经建立；
- Sa-Token 包路径、验证码事务、主键更新、开发数据源、Redis 数据库、Mapper 扫描和资料字段边界已经修复；
- v0.1.2 OpenAPI 成为唯一契约来源，成功码和 Token 方向与实现一致。

### 验证资产

- 手机号安全、请求约束、资料边界和字符串身份单元测试；
- 四张表、七字段、32 位 ID、审计时间、触发器和唯一约束数据库断言；
- Maven、MySQL、Redis、Gateway、App 和接口联合工作流；
- 验证码五次错误锁定、协议缺失回滚、自动注册、登录、资料、退出和日志敏感信息场景；
- SERVER-CHECK-002，结论 `conditional_pass`；
- TASK-011，状态 `blocked_external_runtime_evidence`。

## 5. 检查定义与执行证据

本轮明确区分：

```text
代码已实现
≠ 检查已定义
≠ 检查已执行通过
```

当前 GitHub Actions 没有 v0.1.2 运行状态。因此：

- 不能声称 Maven 已通过；
- 不能声称数据库迁移或回滚已通过；
- 不能声称共享 Redis Token 已跨进程验证；
- 不能声称验证码、登录、资料和退出端到端通过；
- 不能将 YouYu 标记为 `single_project_validated`。

## 6. 维护者例外授权

YouYu `DEC-004` 记录了服务端和数据库先行的受控例外：

- 允许数据库和服务端基础实现先行；
- 不代表高保真已经批准；
- 不允许正式 iOS 页面提前进入实现；
- 不允许扩大到其他业务模块；
- 实现与验证状态必须分离。

该例外是人类责任人覆盖阶段检查关卡的可审计证据，而不是删除检查关卡。

## 7. 当前验证缺口

- Maven 测试与打包实际成功日志；
- MySQL 迁移、触发器、索引、约束和回滚实际执行；
- Gateway、App、MySQL、Redis 和内部身份联合运行；
- Redis 故障、配置不一致和会话失效场景；
- 真实短信供应商；
- 高保真逐页批准；
- iOS 网络层、Keychain、页面状态、真机和模拟用户验收；
- 历史安全、网络隔离和采集待审链路关闭；
- 失败、成本、人工修正和 Framework 改进回写。

## 8. 正式参考工程通过标准

只有下列证据完整，才能评估为 `single_project_validated`：

1. 产品、体验和工程事实可追溯且人工批准；
2. Context 可由新 Agent 独立恢复；
3. 修改边界、接口和检查关卡真实生效；
4. 静态、数据库、运行、安全和模拟用户验证完成；
5. iOS 与服务端完成真实端到端路径；
6. 失败、人工修正、成本和遗漏已经记录；
7. 运行结果和 Framework 改进项完成回写；
8. 人类责任人批准最终结论。

当前尚不满足这些条件，正式业务验证保持 `not_started`。

## 9. 下一步

```text
恢复GitHub Actions或等价运行环境
→ 执行账号业务切片联合工作流
→ 回写Maven、MySQL、Redis和接口证据
→ 修复运行问题并完成TASK-011
→ 高保真人工批准
→ iOS正式实现
→ 真机与模拟用户验收
→ Framework成熟度复核
```

历史首轮复核保留在 [REF-CHECK-001](../12_框架项目Context/验证/REF-CHECK-001_YouYu首轮业务参考任务验证.md)，早期 `partial_pass` 不代表当前参考工程通过。

## 10. 与实战仓库的关系

`ai-product-engineering-in-action` 用于内部教学与步骤演示；本目录记录真实参考工程对 Framework 的正式验证证据、缺陷和改进要求。
