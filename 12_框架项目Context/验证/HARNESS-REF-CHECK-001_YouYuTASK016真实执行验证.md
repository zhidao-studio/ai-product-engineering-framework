# HARNESS-REF-CHECK-001：YouYu TASK-016 真实执行验证

```yaml
validation_id: HARNESS-REF-CHECK-001
framework_task: TASK-20260723-029
reference_project: YouYu
reference_task: TASK-016
status: approved_limited
framework_release: v0.1.10
target_release: v0.2.0
framework_result_commit: c858a8d14ba6278cd11d03e6289bbc726fac8079
youyu_result_commit: 8064df6857e881c449a248d1340ed01b6960a551
youyu_context_commit: c0fe7d79d4a9d90679a02543477f2155fae90423
executed_at: 2026-07-23
human_approval_status: approved
human_approval_at: 2026-07-24
human_approval_statement: 接受 B5 的有限结论
```

## 1. 结论

Harness B1 至 B3 已在 YouYu 高风险安全任务 TASK-016 中完成首次真实参考执行：

- 阶段、风险、人工责任和生产禁止范围真实限制了执行；
- 任务控制清单在显式暂存的任务文件上正确识别允许、禁止、高风险和依赖边界；
- 失败停止规则约束两个不同失败类别各只自动修复一轮；
- 证据清单真实记录静态、运行、用户三层证据，并将本地通过与生产安全、正式业务批准分开；
- 任务通过 5 个小步中文提交完成实现、验证和 Context 回写。

维护者已于 2026-07-24 明确接受 B5 的有限结论。最终结论为 `conditional_pass / approved_limited`：允许进入 B6 逐资产成熟度评估，但不自动提升任何资产成熟度，Framework 不升级稳定版本。

## 2. YouYu 提交链

| 提交 | 独立结果 |
|---|---|
| `00900d2b` | 建立任务、设计、控制和证据基线 |
| `a4ea442f` | 完成 Gateway 可信代理解析与内部来源签名 |
| `48ac8dc2` | 完成 App 来源验签和 Redis 三维原子频控 |
| `8064df68` | 完成全量运行、故障注入、模拟器用户回归和证据闭环 |
| `fe0ed925` | 同步 YouYu 当前事实基线 |

## 3. B1：阶段、风险和人工控制

实际效果：

- TASK-016 被标为 `high`；
- iOS 产品代码、高保真、数据库 Schema、nginx、GitHub Actions、生产密钥和生产地址保持禁止；
- 生产代理列表、阈值、发布和安全豁免继续由维护者负责；
- 高保真明确为不适用，因为任务没有改变用户页面、文案和登录流程。

未发现阶段跳跃或生产权限扩大。

## 4. B2：边界和依赖控制

最终暂存内容检查：

```text
任务: TASK-016
风险: high
检查路径数: 13
边界检查通过
```

真实发现：

1. `worktree` 模式会保守地纳入任务开始前已存在的未跟踪文件；
2. 在脏工作区中，这会把用户原有 `.playwright-cli/`、`.zcode/` 误判成当前任务越界；
3. 正确收口方式不是删除、清理或自动忽略用户文件，而是显式暂存任务文件后使用 `staged` 模式；
4. 用户回归需要既有 iOS 自动化脚本，初始控制清单遗漏该验证支持文件，执行时补充最小路径并保持 iOS 产品代码禁止。

因此需要在规范中明确脏工作区的三种模式及验证支持文件的前置登记。

## 5. B3：失败、证据和结论边界

### 失败控制

| 失败类别 | 首次现象 | 自动修复 | 结果 |
|---|---|---:|---|
| `implementation_error` | Gateway 编译失败 | 1 轮 | 通过 |
| `verification_error` | TraceId 数字片段被日志扫描误报为手机号 | 1 轮 | 完整复验通过 |
| `environment_error` | 模拟器处于 Shutdown | 环境恢复，不修改代码 | 继续执行 |
| `verification_drift` | UI 脚本仍使用旧协议标签和坐标 | 更新验证脚本，产品代码不变 | 认证路径退出码 0 |

前两个不同失败类别均遵守高风险任务一轮自动修复上限。

### 三层证据

| 层 | 实际证据 | 结果 |
|---|---|---|
| 静态 | Shell、任务边界、证据结构、日志规则、补丁检查 | `passed` |
| 运行 | 59 项相关测试、Maven、MySQL、Redis Lua、Gateway/App、Redis 不可达失败关闭 | `passed` |
| 用户 | iPhone 17 Pro Max 模拟器验证码登录、协议、账号信息、退出 | `passed` |
| 发布 | 生产代理、阈值和目标环境未执行 | `not_executed` |

YouYu 证据清单使用：

```text
overall_result: conditional_pass
formal_business_validation: not_executed
```

这证明 Framework 的结构检查允许“三层工程证据均通过，但人工或发布结论仍未完成”的有限表达，没有被迫把任务夸大为生产通过。

## 6. 验证成本与收益

可核验成本：

- 5 个 YouYu 小步提交；
- 2 个正式失败记录；
- 1 次工作区模式误判及改用 `staged`；
- 1 次模拟器环境恢复；
- 1 次用户回归脚本适配；
- 1 份专项验证记录和 1 份机器证据清单。

收益：

- 防止信任客户端伪造来源头；
- 防止用代码存在代替运行证据；
- 防止 Redis 故障时失败开放；
- 防止本地通过扩大成生产安全通过；
- 防止边界检查误处理用户已有未跟踪文件；
- 通过用户层回归发现自动化脚本已落后于已批准体验。

## 7. Framework 候选修订

本轮只修订经真实问题证明的内容：

1. 任务边界规范增加脏工作区与 `worktree/staged/range` 使用规则；
2. 任务规划必须前置列出验证脚本、证据文件和 Context 回写路径；
3. 用户证据优先使用可访问性标签和状态断言，避免只靠固定坐标；
4. 长时运行服务必须由可控生命周期托管，不能假设启动 shell 退出后后台进程仍存活；
5. 失败记录要区分代码、验证规则、环境和验证漂移，避免把不同根因误算成同类无限重试。

## 8. 维护者确认

维护者确认语句：

```text
接受 B5 的有限结论
```

确认范围：

- 接受 TASK-016 的 `conditional_pass` 有限结论；
- 接受进入 B6 逐资产成熟度评估；
- 不等于批准生产代理、生产阈值、正式发布或生产安全；
- 不等于自动将 Harness 资产提升为 `single_project_validated`；
- 具体成熟度和里程碑 B 退出仍需 B6 证据与人工批准。
