---
name: controlled-task-validation
description: "检查受控工程任务的修改边界、风险授权和验证证据，并形成不过度扩大的有限结论。用于提交前、提交后或 PR 复核，前提是仓库已经具备当前任务 Context、任务控制清单、验证证据清单，以及项目内的边界和证据检查器。"
---

# 受控任务验证

验证一次任务是否在批准范围内执行，并检查证据结构能否支撑声明的结论。保持 Harness 为权威规则；不要在 Skill 内复制或放宽项目规则。

## 准备输入

取得以下输入，否则停止并说明缺失项：

- Git 仓库路径；
- 当前项目、阶段和任务 Context；
- 与任务 ID、风险等级和基线一致的任务控制清单 JSON；
- 验证证据清单 JSON；
- 边界检查器和证据检查器路径；优先使用项目内入口，也可使用任务 Context 明确批准的 Framework 权威入口；
- `worktree`、`staged` 或 `range` 检查模式；
- `range` 模式的基线与目标提交；
- 命中高风险路径时的人工授权记录。

确认两个检查器均为项目规则或任务 Context 明确批准的 Framework 权威入口。缺少批准记录或检查器不可用时输出 `blocked`；不要复制脚本，也不要临时编写替代规则。

## 执行流程

1. 读取仓库级 Agent 指令和当前 Context，确认事实源、任务状态和人类责任人。
2. 对照项目风险规范复核任务风险；不得自行降低风险等级。
3. 检查任务 Context、控制清单和证据清单中的任务 ID、基线和风险是否一致。
4. 选择边界模式：
   - 使用 `worktree` 盘点干净工作区；
   - 使用 `staged` 检查脏工作区中显式暂存的当前任务文件；
   - 使用 `range` 复核提交、PR 或历史范围。
5. 调用已批准的边界检查器并保留命令、退出码和输出。检查器位于目标仓库外时必须显式传入 `--repo`，并在任务 Context 记录其来源。Framework 默认入口：

   ```bash
   python3 "<边界检查器路径>" \
     --repo "<目标仓库路径>" \
     --manifest "<任务控制清单>" \
     --mode "<worktree|staged|range>"
   ```

   `range` 模式按需增加 `--base` 和 `--head`。
6. 调用已批准的证据检查器并保留命令、退出码和输出。Framework 默认入口：

   ```bash
   python3 "<证据检查器路径>" \
     --manifest "<验证证据清单>"
   ```

7. 单独复核机器检查无法证明的语义：
   - 修改是否符合任务目标；
   - 高风险授权是否真实且仍有效；
   - 证据内容是否真实；
   - 用户体验、数据和外部副作用是否符合预期。
8. 形成有限结论，列出未验证范围和需要人工确认的事项。
9. 回写任务 Context、验证记录和项目 Context。需要产品、权限、发布、法律或范围决定时停止等待人工确认。

## 处理失败

- 任务 Context 与机器清单不一致：停止，修复事实源后重跑。
- 命中禁止或未批准高风险路径：停止，不扩大允许范围。
- 脏工作区归属不清：保留用户改动，切换到 `staged` 或 `range`。
- 必需证据未通过：禁止输出总体 `passed`。
- 首次出现任务范围内的确定性问题：允许修复一次并复验。
- 同类问题重复、范围扩大或需要新决策：停止并升级给人类责任人。

不要自动批准高风险变更，不要自动发布、回滚生产环境或替代用户验收。

## 输出结果

按以下结构报告：

```yaml
skill: controlled-task-validation
task_id:
repository:
mode:
risk_level:
task_context_status:
boundary_check:
  status: passed | failed | blocked
  command:
  exit_code:
  evidence:
evidence_manifest_check:
  status: passed | failed | blocked
  command:
  exit_code:
  evidence:
human_review_required:
human_review_reasons: []
overall_result: passed | conditional_pass | failed | blocked
unverified_scopes: []
context_updates: []
```

`passed` 只表示本 Skill 负责的边界和证据约束满足，不表示代码正确、用户接受或具备发布条件。发布层未执行时必须明确写入 `unverified_scopes`。

## 回写分类

- 事实缺失或冲突：回写 Context；
- 权威规则或检查器不足：回写 Harness；
- 触发、输入选择、步骤装配或输出表达不清：改进 Skill；
- 产品取舍、高风险授权、验收或发布决定：交给人类责任人。

保持候选能力边界：不执行依赖评估、完整安全审计、OpenAPI 与 Schema 全链一致性、自动回滚、生产发布或多 Agent 编排。
