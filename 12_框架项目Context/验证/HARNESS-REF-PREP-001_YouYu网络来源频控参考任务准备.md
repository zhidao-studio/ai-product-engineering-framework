# HARNESS-REF-PREP-001：YouYu 网络来源频控参考任务准备

```yaml
check_id: HARNESS-REF-PREP-001
status: passed
framework_task: TASK-20260723-028
youyu_task: TASK-016
framework_baseline: a6715ef
youyu_baseline: 50d9a1b626b7519f6ae3290d94b975c481604ab5
youyu_task_commit: 00900d2b
verified_at: 2026-07-23
reference_execution: not_started
```

## 1. 选择结果

选择 YouYu `TASK-016：以 Harness 验证方式实现验证码可信网络来源频控`，它取代旧 TASK-012 作为当前执行包。

选择原因：

- 是账号与“我”已验收切片的真实安全缺口；
- 同时涉及 Gateway、内部签名、App、Redis、错误响应和用户登录回归；
- 可以验证 B1 风险分级、B2 修改边界、B3 一致性与证据控制；
- 不需要扩展页面或新业务模块，高保真有明确不适用依据；
- 不依赖生产发布，可以在本地和目标设备取得证据；
- 代码、Redis TTL 和原路径回归提供可控回滚。

## 2. 已建立的 YouYu 资产

- 工程设计：可信代理链、内部签名、Redis 原子控制、数据边界；
- TASK-016：目标、允许与禁止范围、风险、验收、重试和回滚；
- 任务控制清单：高风险路径显式批准，数据库、iOS、Claw、nginx 和 GitHub Actions 禁止修改；
- 验证证据清单：静态、运行和用户三层初始状态均为 `not_executed`；
- YouYu 项目 Context 和当前阶段已切换到 TASK-016。

## 3. 准备验证

| 检查 | 结果 |
|---|---|
| YouYu 证据清单结构 | 通过，三层均保持 `not_executed` |
| TASK-016 暂存路径边界 | 7 个路径通过 |
| JSON 解析 | 通过 |
| Markdown 本地链接 | 5 个变更文件、39 个链接通过 |
| 补丁检查 | 通过 |
| 提交和推送 | `00900d2b` 已进入 YouYu `main` |

## 4. 边界

- 这只证明参考任务准备完成，不证明网络来源频控已经实现；
- 生产代理列表、生产阈值和生产发布仍需目标环境责任人批准；
- GitHub Billing 按维护者决定暂不检查；
- YouYu 已有 `.playwright-cli/` 和 `.zcode/` 未跟踪目录未读取、未修改、未提交；
- Framework 资产成熟度不变。

## 5. 结论

B4 参考任务准备通过，可以进入 YouYu TASK-016 的真实受控执行。正式参考验证仍为 `not_started`。
