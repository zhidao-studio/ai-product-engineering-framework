# TASK-20260712-001：建立 Framework 自身 Context 基线

```yaml
task_id: TASK-20260712-001
task_context_pack_version: 1.1
title: 建立 Framework 自身 Context 基线
status: completed
project: AI Product Engineering Framework
lifecycle_stage: 工程规格设计
risk_level: medium
owner: 项目维护者
executor: ChatGPT
reviewer: Context 完整性检查与全量 Review
human_approver: zhidao-studio
project_context_pack_version: 0.2-A.2
stage_context_pack_version: 1.1
source_commit: 003616b32edf057fb33db1fcb7c7c3e6a7565219
created_at: 2026-07-12
completed_at: 2026-07-12
```

## 1. 目标与价值来源

### 问题

Framework 已建立 Context 规范和候选模板，但尚未用自身项目验证。若框架不能管理自己的事实、阶段和任务，就不应直接要求业务项目采用。

### 目标

建立本仓库的项目 Context Pack、v0.2.0 / A 阶段 Context、任务记录和完整性检查，使新的人员或 Agent 能够不依赖历史会话恢复当前项目认知。

### 不做

- 不选择业务参考工程；
- 不建设自动 Context 装配器；
- 不建设 Harness 脚本；
- 不把自应用结果标记为跨项目稳定结论。

## 2. 权威事实引用

| 事实 | 来源 | 状态 | 用途 |
|---|---|---|---|
| Framework 愿景与边界 | `01_框架定义/` 四份宪法文档 | active | 确认项目身份和边界 |
| 三平面与十阶段 | `02_全局模型/AI产品工程全局框架.md` | active | 确认全局结构 |
| 设计决策索引 | `11_设计决策/README.md` | active | 恢复演进原因 |
| Context 模型 | `DEC-006` 与 `04_Context工程/` | active | 指导 Pack 建设 |
| 自应用顺序 | `DEC-007` | active | 确认验证边界 |
| 版本体系 | `DEC-008` 与版本管理规范 | active | 区分稳定版本、目标版本和 Pack 版本 |
| 当前 Roadmap | `10_版本演进/Roadmap.md` | active | 确认阶段和下一步 |

## 3. 前置条件

- [x] v0.1.1 全量复核完成；
- [x] 重复事实源已经删除；
- [x] 十阶段生命周期已经统一；
- [x] Context 规范和候选模板已经建立；
- [x] DEC-007 已批准自应用验证；
- [x] DEC-008 已统一版本和里程碑语义。

## 4. 允许修改范围

```text
允许新增或修改：
- 12_框架项目Context/**
- 11_设计决策/README.md
- README.md 中的导航和当前状态
- AGENTS.md 中的当前 Context 入口
- 10_版本演进/**
- CHANGELOG.md
- 08_模板资产/Context/**（仅根据自应用和 Review 发现修正）
- 04_Context工程/**（仅根据明确问题修正）
```

## 5. 禁止修改范围

```text
禁止：
- 改变框架宪法和三平面模型
- 改变十阶段生命周期
- 进入 Harness 自动化实现
- 创建完整 Skill 库
- 引入新的运行依赖
- 将候选模板标记为稳定
```

## 6. 必须保持的契约

- Context 使用四级作用域与独立回写层；
- Pack 只作为入口和快照，不替代权威事实源；
- 设计决策仍保存在 `11_设计决策`；
- Framework 自应用不替代业务参考工程验证；
- 重要修改使用中文提交；
- 稳定版本、目标版本、里程碑和 Pack 版本独立表达。

## 7. 验收断言

- [x] 项目 Context Pack 能回答 Framework 是什么、不是什么；
- [x] 能定位四份宪法、全局模型和设计决策；
- [x] 能说明当前稳定版本、目标版本和当前里程碑；
- [x] 能说明 Context、Harness、Skills、Agents、Loop 的关系；
- [x] 阶段 Context 能列出必要产物、退出门禁和阻塞项；
- [x] 任务 Context 明确允许与禁止修改范围；
- [x] 有独立 Context 完整性检查结果；
- [x] 不复制核心文档正文形成新的平行事实源；
- [x] 由项目维护者确认自应用结果可接受。

## 8. 验证方式与结果

| 验证 | 方法 | 结果 |
|---|---|---|
| 路径验证 | 逐一读取项目 Context 中的核心链接 | 通过 |
| 口径验证 | 对比 README、AGENTS、全局模型、DEC-005 | 十阶段一致 |
| 决策验证 | 读取 DEC-001 至 DEC-008 索引 | 重要变化可恢复 |
| 重复检查 | 检查已知重复目录和文件 | 未发现已知平行事实源 |
| Context 检查 | 使用完整性检查清单 | P0 全通过，93/100 |
| 全量 Review | 检查全仓库内容、版本、状态和模板 | 发现问题已进入 v0.1.1 修订 |
| 人工复核 | 项目维护者要求继续 Review、版本修订和下一阶段 | 接受 |

## 9. 风险与停止条件

- 如发现新的平行事实源，停止并先收敛目录；
- 如 Pack 需要复制大量正文才能理解，回到项目 Pack 规范调整；
- 如核心链接不存在，修复后重新检查；
- 如需要改变宪法或十阶段模型，必须停止并新建设计决策；
- 最大自动修正轮次：2 次，超过后提交项目维护者判断。

## 10. 回写目标与完成情况

| 结果 | 回写位置 | 状态 |
|---|---|---|
| 自应用检查结论 | `12_框架项目Context/验证/` | 已完成 |
| 发现模板遗漏 | `08_模板资产/Context/` 和对应规范 | 已修正版本与状态字段 |
| 发现版本语义问题 | `10_版本演进/版本管理规范.md`、DEC-008 | 已完成 |
| 当前阶段变化 | 项目 Context、阶段 Context、Roadmap | 已完成 |
| 版本进展 | CHANGELOG | 已完成 |

## 11. 执行结果

### 新增或更新的核心资产

- Framework 自身项目 Context Pack；
- v0.2.0 / A 阶段 Context；
- 本任务 Context Pack；
- CTX-CHECK-001；
- 版本管理规范和 DEC-008；
- v0.1.1 全量复核报告；
- 统一状态与 Pack 版本字段。

### 保持不变

- 框架宪法；
- 三平面全局模型；
- 十阶段生命周期；
- 五大 AI 工程基础设施定义。

### 人工确认结论

项目维护者已要求在全量 Review 后进入下一阶段，并明确要求将 v0.1 的 Review 修订升级为 v0.1.1。该指令作为本任务的人工接受依据。

## 12. 未解决事项

- 业务参考工程尚未选择；
- 候选模板仍需真实业务任务验证；
- 链接、状态和版本检查尚未自动化；
- 不同 AI 平台的实际加载方式尚未验证；
- 开源许可证尚未由维护者决定。
