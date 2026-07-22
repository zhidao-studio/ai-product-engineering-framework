# 参考工程

> 参考工程用于证明 Framework 能够控制真实产品交付，而不是只形成文档。当前状态以 [Framework 项目 Context](../12_框架项目Context/README.md) 为准。

## 1. 当前参考工程：YouYu

```text
YouYu版本：v0.1.4
当前里程碑：A / Context 可执行化
当前工作段：A2 / YouYu正式业务验证回写与资产成熟度评估
首个业务切片：手机号验证码登录注册与个人资料管理
产品规则：confirmed
体验定义：confirmed
高保真：v0.1.2 / maintenance_approved
数据库迁移：conditional_pass
OpenAPI：implemented_for_v0.1.4
服务端实现：conditional_pass
静态复核：conditional_pass
运行验证：conditional_pass
iOS正式实现：merged_to_main_core_path_validated
正式业务验证：passed_core_path_by_maintainer
Context模板族成熟度：candidate
项目Context模板：single_project_validated
任务Context模板：single_project_validated
数据库规范成熟度：single_project_validated
Harness里程碑B：not_started
```

## 2. 已完成的完整核心链路

```text
产品定义与不做清单
→ 用户流程与页面状态
→ 高保真 v0.1.2 维护者批准
→ 工程规格、数据库迁移与 OpenAPI
→ TASK-013 受控实现
→ 服务端、本地数据库、Redis 和接口运行验证
→ iOS 严格模拟器路径
→ 真机构建、安装、启动和维护者操作验收
→ PR #3 合并到 main
→ 项目 Context 与 Framework 回写
```

维护者于 2026-07-22 在真机确认“账号和我验证通过”。YouYu 当前 `main` 为 `f2685d66`，PR #3 合并提交为 `047cf099`。

## 3. 通过范围

- 手机号验证码登录或自动注册；
- 协议确认和 App 内协议阅读；
- Keychain Token 保存、恢复和清理；
- 已登录与未登录“我”；
- 账号信息、昵称和个人简介；
- 退出及旧 Token 失效；
- 已批准高保真核心页面与协议行对齐；
- Maven、MySQL、Redis、Gateway、App 和 iOS 开发环境核心路径。

## 4. 未通过或未覆盖范围

- 真机相册、拍照、裁剪、头像上传和受保护头像显示专项；
- 异常网络、服务失败、深色模式、小屏、动态字体和 VoiceOver 专项；
- Redis 故障和网络分区；
- 完整短信 Outbox、网络来源频控和真实短信；
- Token 与数据库事务一致性；
- 历史敏感信息等既有安全事项；
- 正式法律协议、生产部署和发布批准；
- GitHub Billing 与计划额度检查（维护者决定暂缓）。

## 5. 对 Framework 的验证结果

| Framework 资产或假设 | 结果 | 说明 |
|---|---|---|
| 项目 Context Pack | 单项目已验证 | 支撑跨会话恢复与动态事实索引；提交字段更新成本仍需改进 |
| 任务 Context Pack | 单项目已验证 | TASK-013 串联范围、实现、验证、批准、PR 与回写 |
| 阶段 Context | 未通过成熟度提升 | YouYu 阶段文件未随执行和验收持续更新 |
| 冲突记录 | 继续候选 | 有真实安全冲突，但未完成关闭复验 |
| 经验回写 | 继续候选 | 有候选经验，尚未完成统一采纳与效果复验 |
| 数据库基础规范 | 单项目已验证 | 在账号域迁移、触发器、检查和业务路径中实际使用 |

完整验证记录见 [REF-CHECK-002](../12_框架项目Context/验证/REF-CHECK-002_YouYu账号与我正式业务参考验证.md)。

## 6. 当前结论

YouYu 的账号与“我”切片已经提供正式核心路径参考证据，但这不是整个 YouYu 项目、生产安全或 Framework 全部资产的通过结论。

A2 保持 `active`，Context 模板族整体保持 `candidate`，Harness B 保持 `not_started`。下一步先补 Context 成本记录、修复阶段 Context 漂移并由维护者审查 A2 退出。

## 7. 反馈入口

- [从高保真到真机验收](YouYu账号切片反馈_从高保真到真机验收.md)；
- [历史首轮业务参考验证](../12_框架项目Context/验证/REF-CHECK-001_YouYu首轮业务参考任务验证.md)。
