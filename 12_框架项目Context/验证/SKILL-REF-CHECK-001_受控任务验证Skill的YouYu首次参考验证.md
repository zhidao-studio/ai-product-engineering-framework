# SKILL-REF-CHECK-001：受控任务验证 Skill 的 YouYu 首次参考验证

```yaml
check_id: SKILL-REF-CHECK-001
status: conditional_pass
checked_at: 2026-07-24
framework_task: TASK-20260724-033
youyu_task: TASK-017
skill: controlled-task-validation
skill_maturity: candidate
youyu_result_commit: d4ab69a7a3ed9d47ee7e83691b5fa80dd301c9e1
formal_business_validation: not_executed
human_approval: pending
```

## 1. 参考任务

YouYu 使用候选 Skill 执行“账号与‘我’明暗模式、小屏和基础可读性专项验证”。任务是已交付业务切片的真实未完成专项，只验证，不修改产品、高保真、接口、数据库、iOS 业务代码或服务端。

## 2. Skill 实际执行

### 2.1 预检与首次失败

首次按候选 Skill 原文执行时，YouYu 没有项目内检查器，因此正确输出 `blocked`。复核确认这不是 YouYu 产品问题，也不是 Harness 规则错误，而是 Skill 的输入与装配规则过窄：

```text
原规则：只接受目标仓库内检查器
真实需要：项目内检查器，或任务明确批准的 Framework 权威检查器
```

候选 Skill 完成最小修订后：

- 外部检查器必须由任务 Context 明确批准；
- 边界检查必须显式传入目标仓库 `--repo`；
- 缺少批准时仍然 `blocked`；
- 不复制、不改写、不放宽 Harness 权威规则。

修订使用官方 `quick_validate.py` 验证通过，未新增依赖。

### 2.2 受控任务与检查

YouYu 在 `a28094ee` 建立 TASK-017、任务控制清单和证据清单。在最终证据回写前后，权威检查器实际执行：

```text
任务边界检查：passed / exit 0
证据清单检查：passed / exit 0
overall_result：conditional_pass
```

任务只修改控制清单允许的 Context 和验证资产；`.playwright-cli/`、`.zcode/` 以及产品、代码、配置和依赖均未修改。

## 3. 真实验证结果

| 层 | 证据 | 结果 |
|---|---|---|
| 静态 | 系统语义色检查；两台模拟器 Debug 构建 | `passed` |
| 运行 | iPhone 17 Pro Max 与 iPhone 16e 构建、安装、启动；隔离视觉 Mock 导航 | `passed` |
| 用户路径 | 五类页面或状态在浅色、深色和小屏条件下可到达并检查 | `passed` |
| 总体 | 只覆盖模拟器基础布局与可读性 | `conditional_pass` |

专项未发现关键控件不可达、严重截断、覆盖或主要文字不可辨认。构建存在依赖弃用提示和既有 Swift 并发隔离警告，不阻止本次视觉专项，但应由后续独立代码任务处理。

## 4. 结论边界

```yaml
overall_result: conditional_pass
verified_scopes:
  - 两台iOS26.3模拟器构建与启动
  - 浅色与深色模式
  - 390pt小屏
  - 登录前后我、登录、编辑资料、账号信息与退出确认
unverified_scopes:
  - 真机视觉专项
  - 动态字体
  - VoiceOver
  - 异常网络与服务异常
  - 真实后端、数据库与短信
  - 生产与发布
human_approval: pending
```

隔离视觉 Mock 位于 YouYu 仓库外，只用于页面导航，不能替代真实后端或正式业务验证。

## 5. 对 Framework 的反馈

### Skill

- 检查器来源装配已获得真实参考证据；
- `--repo` 要求能防止跨仓库检查落到错误工作目录；
- 候选 Skill 可以在不复制 Harness 规则的前提下完成真实项目装配。

### Harness

- 权威任务边界与证据检查器行为符合预期；
- 本轮没有发现需要修改 Harness 规则或脚本的问题。

### Context

- 任务 Context 显式批准外部检查器，是跨仓库能力装配所需事实；
- 证据清单能把三层证据与总体有限结论分开；
- `/tmp` 运行证据必须登记路径、用途和不覆盖范围，不能把临时证据提交到产品仓库。

### 产品与工程

- 本轮未发现必须修改产品或高保真的问题；
- Swift 并发隔离警告属于后续代码质量事项，不应在纯验证任务中顺手修复。

## 6. 成熟度判断

`controlled-task-validation` 已完成 Framework 自应用和一个 YouYu 真实任务参考验证，但仍只有一个参考工程，也尚未完成维护者对 C3 有限结论的确认。因此成熟度继续为：

```text
candidate
```

不得提升为 `single_project_validated`、跨项目或稳定。
