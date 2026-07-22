# TASK-20260722-023：记录 Context 成本并修复阶段 Context 漂移

```yaml
task_id: TASK-20260722-023
status: completed
project: AI Product Engineering Framework
stage: 运行反馈与持续迭代
risk_level: medium
owner: zhidao-studio
executor: Codex
human_approver: 项目维护者
framework_baseline_commit: 7a23cb5d2aec02d10d993f861ac54380fff925e7
reference_project: YouYu
reference_baseline_commit: f2685d66c2f7733f160f11d1e93c9726aebd61d1
reference_source_commit: 50d9a1b6e110fbe2f64fb89a1cdbca00ab13d474
framework_source_commit: a302a9fd796d479a08d1d99ae211aff4ef8ce9ea
created_at: 2026-07-22
```

## 1. 目标

完成 A2 里程碑退出前的工程收尾：记录 YouYu 账号与“我”切片的 Context 维护成本、主要人工修正和遗漏；修复阶段 Context 在项目从准备、执行到验收过程中未同步更新的问题；用 YouYu 当前阶段复验修订后的模板。

## 2. 允许修改

### YouYu

- `05_项目Context/阶段/`；
- `05_项目Context/项目Context.md`；
- `05_项目Context/经验回写/`；
- 当前 Context 索引与必要状态摘要。

### Framework

- 阶段 Context 规范与模板；
- Framework 当前项目 Context、A 阶段 Context、Roadmap 和 Context 专题状态；
- 新增 `CTX-CHECK-002` 与任务结果回写。

## 3. 禁止修改

- 不修改 YouYu iOS、服务端、Claw、数据库、接口或运行配置；
- 不升级 YouYu 或 Framework 的稳定版本；
- 不检查或恢复 GitHub Billing 与计划额度；
- 不启动 Harness 里程碑 B；
- 不把账号与“我”核心路径通过扩大为全部专项、生产安全或发布通过；
- 不修改 `ai-product-engineering-in-action`；
- 不把估算值伪装成精确 Token、工时或费用。

## 4. 实施要求

1. 将 YouYu “业务功能准备阶段”标为历史快照，并链接当前阶段；
2. 新建 YouYu “质量与安全验证阶段”Context，引用 TASK-013、UAT-001、PR #3 和当前未完成专项；
3. 以可追溯事件计数记录人工修正和遗漏；无法取得的 Token、工时和费用明确标为 `not_measured`；
4. 阶段 Context 模板增加来源提交、最近确认、过期条件、更新触发和替代关系；
5. 规定阶段变化、任务完成、人工批准、PR 合并和项目 Context 阶段变化必须触发阶段 Context 复核；
6. 在 YouYu 当前阶段复验模板，并形成 `CTX-CHECK-002`；
7. 保持项目、阶段和任务 Context 的状态、链接和提交字段一致。

## 5. 验收断言

- [x] YouYu 当前阶段入口不再指向业务功能准备；
- [x] 历史阶段不会与当前阶段并列有效；
- [x] Context 成本、人工修正和遗漏有证据边界；
- [x] 阶段 Context 模板具备可检查的过期与更新触发字段；
- [x] YouYu 实例满足修订后的阶段模板 P0 字段；
- [x] `CTX-CHECK-002` 给出通过、限制和成熟度结论；
- [x] A2 是否可退出仍保留维护者批准；
- [x] 两个仓库相关检查通过并分别使用中文提交推送 `main`。

## 6. 预期结论边界

本任务可以使阶段 Context 模板获得一次修订后的 YouYu 复验证据，但是否提升其成熟度必须由证据决定；不得为了完成 A2 人为写成 `single_project_validated`。

## 7. 结果

### YouYu 结果

- TASK-015 已完成并推送 `main`；
- 当前阶段切换为“质量与安全验证”，历史准备阶段已归档；
- EXP-005 记录项目 Context 同期 23 次提交、阶段目录 0 次提交和至少 8 个明确修正事件；
- Token、人工工时和模型或工具费用标为 `not_measured`；
- 最终参考提交为 `50d9a1b6e110fbe2f64fb89a1cdbca00ab13d474`。

### Framework 结果

- 阶段规范、模板和完整性检查清单已增加防漂移字段；
- CTX-CHECK-002 为 `passed_current_stage_revalidation_with_transition_pending`；
- 阶段模板继续保持 `candidate`，因为修订后尚未经历下一次真实阶段转换；
- A2 工程退出条件已满足，唯一剩余条件为维护者批准；
- Harness B 保持 `not_started`，稳定版本保持 `v0.1.10`。

### 验证

- 两个仓库 `git diff --check`：通过；
- 变更 Markdown 本地链接检查：通过；
- Framework `scripts/check-release-state.sh`（绑定 YouYu 仓库）：通过；
- 未修改任何业务代码、数据库、运行配置或 Billing 设置。
