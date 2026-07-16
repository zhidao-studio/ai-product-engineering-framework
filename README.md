# AI 产品工程框架

> **AI Product Engineering Framework**：由 zhidao-studio 专有维护、跨平台、可验证的 AI 产品工程框架。它用工程化方式组织人、AI Agent、Context、Skills、检查关卡和反馈闭环，将产品目标持续转化为可维护、可验证、可演进的软件产品。

> **专有权利声明：** 本仓库不是开源项目。未经 zhidao-studio 事先书面授权，禁止使用、复制、修改、分发、商业化、模型训练或创建衍生作品。正式条款见 [LICENSE](LICENSE)。

![AI 产品工程框架 v0.1 概念总览](assets/图片/AI产品工程框架v0.1概念总览.png)

## 当前版本

```text
当前稳定版本：v0.1.8
目标开发版本：v0.2.0
当前里程碑：A / Context 可执行化
当前工作段：A2 / YouYu v0.1.2 运行验证待执行
执行状态：active
YouYu版本：v0.1.2
服务端实现：implemented_not_runtime_validated
静态复核：conditional_pass
自动检查：defined / not_executed
高保真：v0.1.0-draft.6 / conditional_pass / 待维护者批准
正式业务验证：not_started
Context模板：candidate
数据库规范：candidate
Harness里程碑B：not_started
仓库可见性：Public，待维护者手动切换 Private
```

当前状态的唯一入口：[Framework 项目 Context](12_框架项目Context/README.md)。

- [v0.1.8 YouYu 验证加固同步报告](10_版本演进/v0.1.8YouYu验证加固同步报告.md)
- [Roadmap](10_版本演进/Roadmap.md)
- [CHANGELOG](CHANGELOG.md)
- [版本管理规范](10_版本演进/版本管理规范.md)

## v0.1.8 更新

Framework 同步了 YouYu `v0.1.2` 的验证加固：

- 修正 Sa-Token 编译包路径；
- 修正验证码错误次数与过期状态被事务回滚的问题；
- 将账号、资料和协议记录更新收敛到主键和最小字段；
- 统一 Admin、App、Gateway 的共享 Redis 数据库配置；
- 补齐 App MySQL 数据源和明确 Mapper 扫描；
- 修正成功码、Token 响应、资料字段和未知 JSON 字段契约；
- 新增安全、请求、资料和字符串身份单元测试；
- 新增数据库结构断言和账号业务切片联合工作流；
- 新增 SERVER-CHECK-002，结论为 `conditional_pass`；
- TASK-011 因缺少运行证据保持阻塞。

本轮最重要的事实约束：

```text
代码已实现
≠ 检查已定义
≠ 检查已执行通过
```

GitHub Actions 当前没有 YouYu v0.1.2 的运行状态，因此 Framework 不把自动检查文件写成 Maven、数据库、共享会话或接口已经通过。

## 这是什么

本项目不是 Prompt 合集、Coding Skill 收藏库，也不是某个模型或 Agent 平台的配置示例。

它回答的是：

> 当 AI Agent 已能执行复杂任务时，人和团队如何定义目标、管理 Context、约束执行、验证结果，并通过真实反馈持续改进产品？

框架包含三个平面：

1. **产品价值生命周期**：从价值验证到持续迭代；
2. **AI 工程基础设施**：Context、Harness、Skills、Agents、Loop；
3. **治理与组织记忆**：决策、版本、安全、权限、质量、成本和变更。

```mermaid
flowchart TB
    H[人类目标、价值判断与最终责任]
    L[产品价值生命周期]
    I[AI工程基础设施]
    G[治理与组织记忆]
    P[可交付、可维护、可验证、可演进的软件产品]
    H --> L
    I -.支撑.-> L
    G -.约束并记录.-> L
    L --> P
```

## 框架宪法

| 文档 | 回答的问题 |
|---|---|
| [愿景与定位](01_框架定义/AI产品工程框架愿景与定位.md) | 框架为什么存在、是什么、不是什么 |
| [适用场景与期望](01_框架定义/适用场景与期望.md) | 哪些项目适用、实施多深 |
| [核心原则](01_框架定义/AI产品工程核心原则.md) | 新能力必须满足什么判断标准 |
| [边界声明](01_框架定义/AI产品工程边界声明.md) | 框架、人和 AI 分别负责什么 |

重大变化必须进入 [设计决策](11_设计决策/README.md)，局部实现不得静默修改宪法层。

## 十阶段产品价值生命周期

| 阶段 | 核心问题 |
|---|---|
| 1. 战略与价值验证 | 为什么值得做 |
| 2. 产品定义 | 做什么与不做什么 |
| 3. 用户体验设计 | 用户如何完成目标 |
| 4. 高保真预览与确认 | 最终体验是否正确 |
| 5. 工程规格设计 | 系统如何实现 |
| 6. 受控任务执行 | AI 可在什么范围完成什么 |
| 7. 质量与安全验证 | 系统是否正确、可靠和安全 |
| 8. 模拟用户验收 | 真实用户路径是否可用 |
| 9. 发布交付 | 是否具备进入目标环境条件 |
| 10. 运行反馈与持续迭代 | 真实使用如何改变下一轮 |

## 五大 AI 工程基础设施

| 基础设施 | 核心问题 |
|---|---|
| Context Engineering | AI 凭什么理解项目 |
| Harness Engineering | 如何限制执行并证明完成 |
| Skill Engineering | 如何把成熟方法封装为重复能力 |
| Agent Engineering | 谁承担责任，如何协作 |
| Loop Engineering | 如何观察、纠偏和沉淀 |

## 当前参考工程

[YouYu](09_参考工程/README.md) 用真实产品切片验证 Framework。

当前已形成：

```text
产品与体验
→ 工程规格
→ 服务端实现
→ 静态缺陷修复
→ 单元测试与数据库断言
→ 联合工作流
→ 等待真实运行证据
```

仍未完成：Maven、MySQL、Redis、Gateway/App 联合运行，高保真批准，iOS、真机与模拟用户验收。因此 YouYu 尚不能作为 `single_project_validated` 证据。

## 文档导航

| 模块 | 说明 |
|---|---|
| [框架定义](01_框架定义/AI产品工程框架愿景与定位.md) | 愿景、原则、边界和术语 |
| [全局模型](02_全局模型/AI产品工程全局框架.md) | 三平面、十阶段和五大基础设施 |
| [角色体系](03_角色体系/人类与AI角色.md) | 人类责任、AI 角色和交接 |
| [Context 工程](04_Context工程/README.md) | 事实源、Context Pack、装配、冲突和回写 |
| [Harness 工程](05_Harness工程/执行控制与检查关卡.md) | 边界、约定、权限和检查关卡 |
| [Skills 与 Agent](06_Skills与Agent/Skills与Agent协作模型.md) | 能力封装和角色协作 |
| [Loop 工程](07_Loop工程/持续反馈与演进闭环.md) | 反馈、失败归因和持续演进 |
| [模板资产](08_模板资产/README.md) | 可执行模板入口 |
| [参考工程](09_参考工程/README.md) | 真实产品验证状态 |
| [版本路线](10_版本演进/Roadmap.md) | 版本与里程碑 |
| [设计决策](11_设计决策/README.md) | 重大取舍和替代条件 |
| [项目 Context](12_框架项目Context/README.md) | 当前状态、阻塞和下一步 |

## 当前边界

- v0.1.8 不代表 v0.2.0 里程碑 A 已退出；
- Context 模板和数据库规范保持 `candidate`；
- Harness B 尚未开始；
- 检查定义不等于检查执行；
- Framework 自应用不替代真实业务验证；
- 专有许可证限制使用权，Private 才能限制仓库访问。

## 贡献与许可

- 受邀协作者：[CONTRIBUTING.md](CONTRIBUTING.md)
- AI 执行规则：[AGENTS.md](AGENTS.md)
- 专有许可证：[LICENSE](LICENSE)

> 当前仓库仍为 Public。要形成真实访问控制，维护者需要在 GitHub 设置中切换为 Private。
