# Harness 模板与机器检查

> 本目录把 Harness 规则转化为一次任务可以直接填写和检查的输入。成熟度逐项记录，检查已定义仍不等于已在当前任务执行通过。

## 当前模板

| 模板 | 用途 | 状态 |
|---|---|---|
| [任务执行控制模板](任务执行控制模板.md) | 连接任务 Context、风险、边界、权限、验证和结果 | `single_project_validated` |
| [任务控制清单模板](任务控制清单模板.json) | 为确定性路径检查提供机器输入 | `single_project_validated` |
| [依赖变更评估模板](依赖变更评估模板.md) | 记录新增、升级、替换或移除依赖的评估和批准 | `candidate` |
| [一致性检查清单模板](一致性检查清单模板.md) | 追溯 OpenAPI、Schema、服务端、客户端和错误码 | `candidate` |
| [验证证据包模板](验证证据包模板.md) | 记录静态、运行、用户和发布证据及有限结论 | `single_project_validated` |
| [验证证据清单模板](验证证据清单模板.json) | 为证据结构和总体结论检查提供机器输入 | `single_project_validated` |
| [失败与回滚记录模板](失败与回滚记录模板.md) | 连续记录失败分类、尝试次数、退回和回滚 | `candidate` |

配套检查器：

| 检查器 | 用途 | 状态 |
|---|---|---|
| `scripts/check_task_boundary.py` | 检查允许、禁止、高风险和依赖文件路径 | `single_project_validated` |
| `scripts/check_evidence_manifest.py` | 检查证据结构和总体结论边界 | `single_project_validated` |

## 使用关系

```text
任务 Context Pack（目标、事实、验收）
        ↓ 引用
任务执行控制模板（风险、权限、检查和结果）
        ↓ 同步关键字段
任务控制清单 JSON（机器路径检查）
        ↓
边界检查结果与人工专项检查
        ↓
一致性清单与验证证据包
        ↓ 同步关键字段
验证证据清单 JSON（机器结论约束）
        ↓
失败、退回、回滚与Context回写
```

任务控制模板不复制产品、接口、高保真和任务目标。它必须引用权威任务 Context，避免形成第二套事实源。

## 当前边界

- 路径脚本只能判断 Git 文件范围；
- 证据脚本只能判断 JSON 结构和结论约束；
- 依赖内容、代码语义、外部状态和用户体验仍需专项检查；
- 高风险授权必须来自人，不能通过修改 JSON 自行批准；
- `single_project_validated` 只表示 YouYu TASK-016 提供了单项目证据；
- 依赖、全链一致性、生产发布和真实回滚相关模板继续保持 `candidate`；
- Harness 模板族整体不打包提升。
