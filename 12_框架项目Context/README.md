# AI 产品工程框架：项目 Context Pack

> 本文件是 `ai-product-engineering-framework` 当前运行状态、阻塞、风险和下一步的唯一入口。README、AGENTS、Roadmap、历史任务、验证和发布报告只提供摘要或历史证据，不得覆盖本文件的当前状态。

```yaml
project_context_id: PROJ-CONTEXT-AIPEF
project: AI Product Engineering Framework
status: active
execution_status: blocked
context_pack_version: 0.2-A.8
owner: zhidao-studio
current_stage: 工程规格设计
current_work_segment: A2 / 正式业务参考工程验证准备
stable_release: v0.1.5
target_release: v0.2.0
current_milestone: A / Context 可执行化
working_branch: main
source_commit: ecbad719073fd30d6aba0c3ddc7220751ceba942
repository_visibility: public_pending_private
license_model: proprietary_all_rights_reserved
last_verified_at: 2026-07-12
sensitivity: proprietary
```

> `source_commit` 是本次 v0.1.5 全仓复核开始时已经核验的远程 `main` 基线。后续发布与元数据提交不改变本次复核所依据的仓库起点。

## 1. 当前结论

| 项目 | 当前结论 |
|---|---|
| 稳定版本 | v0.1.5 |
| 目标版本 | v0.2.0 |
| 当前里程碑 | A / Context 可执行化 |
| 当前工作段 | A2 / 正式业务参考工程验证准备 |
| 里程碑状态 | `active` |
| 当前执行状态 | `blocked` |
| 阻塞原因 | YouYu 前后端代码基础框架仍在整理 |
| YouYu 正式业务验证 | `not_started` |
| YouYu PR #1 | 初步工程证据，不计为正式验证 |
| Context 模板成熟度 | `candidate` |
| Harness 里程碑 B | 尚未正式开始 |
| 仓库可见性 | GitHub 已核验为 Public，待维护者手动切换 Private |

### 已完成的 A1 工作段

- 四级 Context 作用域和独立回写层；
- 事实源、状态、版本、敏感级别和装配规则；
- 项目、阶段和任务 Context Pack 规范；
- 冲突、缺失、过期和经验回写规则；
- Context 完整性检查清单和五类候选模板；
- Framework 自应用检查，P0 通过，历史评分 93/100；
- YouYu PR #1 初步工程证据回写；
- v0.1.1 至 v0.1.5 治理修订。

### 尚未完成的 A2 工作段

- YouYu 整理后 `main` 的完整复核；
- 正式项目 Context、阶段 Context 和任务 Context；
- 产品范围、用户流程和高保真人工确认；
- 接口约定和数据结构约定的唯一权威来源；
- 小而完整的前后端业务切片；
- 静态、运行和模拟用户三层验证；
- Context 填写成本、人工修正、遗漏和任务成本复盘；
- 模板成熟度升级判断；
- 里程碑 A 人工退出批准。

## 2. 项目身份与边界

- **仓库**：`zhidao-studio/ai-product-engineering-framework`；
- **定位**：由 zhidao-studio 专有维护、跨平台、可验证的 AI 产品工程框架；
- **核心问题**：如何让 AI Agent 在人的目标与责任下，跨完整产品生命周期受控、可验证、可持续地参与软件产品生产；
- **默认分支**：`main`；
- **明确不做**：当前不建设通用向量知识库、自动记忆平台、完整 Skill 市场、无人值守 Agent 编排或未经验证的企业级治理平台。

## 3. 权威事实入口

| 主题 | 权威来源 |
|---|---|
| 许可与外部使用 | [LICENSE](../LICENSE) / [DEC-009](../11_设计决策/DEC-009_采用专有闭源许可并限制未经授权使用.md) |
| 愿景与定位 | [愿景与定位](../01_框架定义/AI产品工程框架愿景与定位.md) |
| 适用场景 | [适用场景与期望](../01_框架定义/适用场景与期望.md) |
| 核心原则 | [核心原则](../01_框架定义/AI产品工程核心原则.md) |
| 框架边界 | [边界声明](../01_框架定义/AI产品工程边界声明.md) |
| 中文术语 | [术语与易懂表达规范](../01_框架定义/术语与易懂表达规范.md) |
| 三平面和十阶段 | [全局框架](../02_全局模型/AI产品工程全局框架.md) / [DEC-005](../11_设计决策/DEC-005_拆分模拟用户验收与发布交付阶段.md) |
| Context 四级模型 | [Context 工程](../04_Context工程/README.md) / [DEC-006](../11_设计决策/DEC-006_Context采用四级作用域与独立回写层.md) |
| Harness 当前定义 | [执行控制与检查关卡](../05_Harness工程/执行控制与检查关卡.md) |
| 版本规则 | [版本管理规范](../10_版本演进/版本管理规范.md) / [DEC-008](../11_设计决策/DEC-008_采用语义化发布版本与独立开发里程碑.md) |
| 开发路线 | [Roadmap](../10_版本演进/Roadmap.md) |
| 当前阶段详情 | [v0.2.0 / A 阶段 Context](阶段/v0.2-A_Context可执行化.md) |
| 当前参考工程状态 | [参考工程入口](../09_参考工程/README.md) |

## 4. 当前任务与证据

### 当前任务

| 任务 | 状态 | 入口 |
|---|---|---|
| v0.1.5 当前状态收敛与历史边界治理 | `completed` | [TASK-20260712-007](任务/TASK-20260712-007_发布v0.1.5并收敛当前状态.md) |
| 等待 YouYu 基础框架整理完成 | `blocked` | 外部项目进行中 |
| 复核整理后的 YouYu `main` | `not_started` | 待建立正式任务 Context |
| 建立正式前后端业务切片任务 | `not_started` | 待建立正式任务 Context |

### 当前有效证据

- [v0.1.5 当前状态收敛与历史边界治理报告](../10_版本演进/v0.1.5当前状态收敛与历史边界治理报告.md)；
- [CTX-CHECK-001：Framework 自身 Context 基线](验证/CTX-CHECK-001_Framework自身Context基线.md)，历史自应用证据；
- [REF-CHECK-001：YouYu 首轮初步工程证据](验证/REF-CHECK-001_YouYu首轮业务参考任务验证.md)，历史证据，不代表当前正式验证状态；
- [TASK-20260712-006：修正 YouYu 正式验证状态](任务/TASK-20260712-006_修正YouYu正式验证状态.md)。

> TASK-001 至 TASK-006、CTX-CHECK-001、REF-CHECK-001 和 v0.1.1 至 v0.1.4 报告均为历史快照。文件内的版本、术语、状态和下一步只反映当时判断。

## 5. 风险与阻塞

| 风险或事项 | 是否阻塞 | 当前处理 | 下一决策点 |
|---|---|---|---|
| 仓库仍为 Public | 阻塞真正访问控制 | 已有专有许可，待维护者切换 Private | 立即执行 |
| YouYu 基础框架仍在整理 | 阻塞正式参考任务 | 整理后重新复核 `main` | 正式任务开始前 |
| 正式业务验证尚未开始 | 阻塞模板成熟度升级 | 保持 `candidate` | 里程碑 A 退出前 |
| Context 成本与人工修正数据缺失 | 阻塞模板成本判断 | 正式任务中记录 | 里程碑 A 退出前 |
| PR 人工检查关卡未约束实际合并 | 阻塞检查关卡可信性 | 里程碑 B 建 Required Checks | Harness 可执行化 |
| 链接、版本、状态和元数据仍主要人工检查 | 不阻塞当前等待 | 里程碑 B 建自动检查 | Harness 可执行化 |
| 前后端、OpenAPI 和 Schema 未形成完整闭环 | 阻塞联合验证 | 选择端到端业务切片 | 里程碑 B/C |

## 6. 下一步

```text
YouYu 基础框架整理完成
→ 通读并复核整理后的 main
→ 确认前端、后端、iOS、环境和启动恢复路径
→ 选择一个小而完整的业务切片
→ 建立 YouYu 项目、阶段和任务 Context
→ 确认产品范围、用户流程和高保真
→ 建立接口与数据约定
→ 配置修改边界、检查关卡和人工节点
→ 完成静态、运行和模拟用户三层验证
→ 记录成本、遗漏和人工修正
→ 回写 Framework
→ 决定里程碑 A 是否退出
```

在 YouYu 整理完成前，不继续批量扩写 Context 文档，不提前宣布进入 Harness B，也不升级候选模板成熟度。

## 7. 安全与敏感信息

- 本仓库内容属于专有资产；
- 不得提交密钥、凭据、个人隐私或未授权企业信息；
- 示例数据必须使用合成或脱敏内容；
- GitHub 权限和连接器凭据不得记录在仓库；
- 未经书面授权，不得将仓库内容发送到外部模型、第三方知识库、公共数据集或其他仓库；
- 真实业务参考工程必须单独判断敏感级别、模型使用边界和授权范围。

## 8. 更新记录

| 日期 | 变化 | 关联决策或任务 |
|---|---|---|
| 2026-07-12 | 建立 Framework 自身项目 Context Pack | DEC-007 / TASK-20260712-001 |
| 2026-07-12 | 统一版本、许可和中文术语治理 | DEC-008 至 DEC-010 / v0.1.1 至 v0.1.4 |
| 2026-07-12 | 修正 YouYu 正式验证状态为未开始 | TASK-20260712-006 |
| 2026-07-12 | 收敛当前状态入口、标记历史快照并补充基线提交 | TASK-20260712-007 / v0.1.5 |
