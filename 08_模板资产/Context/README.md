# Context 候选模板

> 本目录提供 Context Engineering 的第一批可复制模板。当前机器成熟度为 `candidate`，需要在真实参考工程中使用、发现问题并复验后，才能升级。

## 模板清单

| 模板 | 用途 | 当前成熟度 |
|---|---|---|
| [项目 Context Pack 模板](项目Context-Pack模板.md) | 建立项目长期记忆入口 | `candidate` |
| [阶段 Context 模板](阶段Context模板.md) | 管理生命周期阶段的输入、产物和退出门禁 | `candidate` |
| [任务 Context Pack 模板](任务Context-Pack模板.md) | 为一次 AI 任务装配目标、事实、边界和验证 | `candidate` |
| [Context 冲突记录模板](Context冲突记录模板.md) | 记录版本、文档、契约和责任冲突 | `candidate` |
| [经验回写记录模板](经验回写记录模板.md) | 将验证、失败和人工修正沉淀为长期资产 | `candidate` |

## 使用规则

1. 复制模板到具体项目，不在 Framework 模板中填写业务内容；
2. 删除不适用项时必须说明裁剪理由，不能删除 P0 控制项；
3. Pack 优先引用权威事实源，不大段复制形成平行版本；
4. 敏感信息必须排除、脱敏或通过受控工具访问；
5. 使用后记录实际遗漏、重复、理解成本和发现的问题；
6. 至少通过一个真实参考工程后，才可以升级为 `single_project_validated`；
7. 进入 `stable` 前必须有跨项目证据、正例、反例和检查清单；
8. YAML 使用统一机器状态和版本字段，正文可以附中文说明。

## 成熟度模型

```text
candidate
→ single_project_validated
→ cross_project_validated
→ stable
→ deprecated
```

| 机器值 | 中文显示 | 使用边界 |
|---|---|---|
| `candidate` | 候选 | 仅试用和收集证据 |
| `single_project_validated` | 单项目已验证 | 可在相似场景参考，不可宣称通用稳定 |
| `cross_project_validated` | 跨项目已验证 | 可申请进入稳定资产 |
| `stable` | 稳定 | 可作为正式框架模板使用 |
| `deprecated` | 已废弃 | 不用于新任务 |

模板状态变化必须记录验证证据；重大结构变化应形成设计决策。
