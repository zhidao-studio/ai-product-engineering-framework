# HARNESS-MATURITY-001：B6 逐资产成熟度评估

```yaml
validation_id: HARNESS-MATURITY-001
task_id: TASK-20260724-030
status: approved_limited
milestone: B / Harness 可执行化
framework_release: v0.1.10
target_release: v0.2.0
framework_baseline_commit: b0b5c7a43946eb518bee5badf0c1d295fb38015c
framework_result_commit: 47bd8ac372f6d5b487044906a017670cf26d9283
youyu_task: TASK-016
youyu_result_commit: 8064df6857e881c449a248d1340ed01b6960a551
youyu_approval_commit: d2c277a710b996186a8eaebc01b23b8fef077bfe
youyu_context_commit: 11c8a65250940552c72213ab0eaddbb9e7825e62
assessed_at: 2026-07-24
assessor: Codex
human_approval_status: approved
human_approval_at: 2026-07-24
human_approval_statement: 继续呢
approval_scope: 接受B6成熟度建议并批准里程碑B以conditional_pass有限退出
```

## 1. 结论摘要

B1 至 B5 已证明一个最小 Harness 闭环能够在 YouYu 高风险任务中实际工作：

```text
风险判断
→ 人工责任和禁止范围
→ 任务路径与高风险授权
→ 静态、运行、用户证据
→ 失败分类和有限重试
→ 有限结论
→ 维护者批准
```

本轮不整包提升 Harness。建议只将“风险分级、任务边界、任务控制清单、证据结构及其确定性检查器”提升为 `single_project_validated`；其余资产继续保持 `candidate`。

里程碑 B 推荐结论为 `conditional_pass / pending_human_approval`。它证明最小 Harness 可执行，不代表生产发布控制、跨项目复用或整个 Harness 资产族稳定。

## 2. 建议提升为单项目已验证

| 资产 | 当前 | 建议 | YouYu 直接证据 | 限制 |
|---|---|---|---|---|
| 风险分级与控制强度 | `candidate` | `single_project_validated` | TASK-016 被判定为 `high`，生产代理、阈值、密钥和发布继续保留人工责任 | 只验证高风险任务，未覆盖其他风险等级 |
| 任务修改边界与权限规范 | `candidate` | `single_project_validated` | 允许、禁止和高风险路径真实生效；脏工作区误报推动 `staged/range` 修订 | 只证明 Git 路径边界，不证明外部副作用 |
| 任务执行控制模板 | `candidate` | `single_project_validated` | TASK-016 串联任务 Context、风险、边界、检查、失败和有限结果 | 只验证一个安全任务 |
| 任务控制清单模板 | `candidate` | `single_project_validated` | TASK-016 控制 JSON 被实际填写并用于提交前检查 | 仍需人工保证清单授权真实性 |
| `check_task_boundary.py` | `candidate` | `single_project_validated` | Framework 自应用、YouYu TASK-016、脏工作区误报和最终 `staged` 检查 | 不检查代码语义、数据库或外部系统 |
| 验证证据与结论边界规范 | `candidate` | `single_project_validated` | 静态、运行、用户均通过，发布未执行，总体仍保持 `conditional_pass` | 未验证生产发布证据 |
| 验证证据包模板 | `candidate` | `single_project_validated` | SECURITY-CHECK-002 按层记录命令、结果、失败和未完成项 | 单项目单任务 |
| 验证证据清单模板 | `candidate` | `single_project_validated` | TASK-016 机器清单记录三个必需层并阻止扩大结论 | 不验证证据内容真实性 |
| `check_evidence_manifest.py` | `candidate` | `single_project_validated` | Framework 正反例测试和 YouYu TASK-016 真实清单检查通过 | 只检查结构和结论约束 |

## 3. 继续保持候选

| 资产 | 结论 | 原因 |
|---|---|---|
| Harness 执行控制与检查关卡总览 | `candidate` | 一个真实任务不能证明整个 Harness 资产族 |
| 阶段进入、退出与退回规范 | `candidate` | B 阶段经历正常转换，但没有真实阶段退回或停止 |
| 依赖与高风险变更授权规范 | `candidate` | TASK-016 没有依赖变更，依赖评估分支未执行 |
| 依赖变更评估模板 | `candidate` | 没有真实依赖新增、升级、替换或移除 |
| 接口、数据与实现一致性规范 | `candidate` | 内部签名链有一致性证据，但没有执行 OpenAPI、Schema、服务端、客户端全链检查 |
| 一致性检查清单模板 | `candidate` | TASK-016 不涉及完整公开接口和数据库 Schema 变更 |
| 安全与敏感信息检查规范 | `candidate` | 日志和密钥边界有证据，但 Git 历史、生产网络和完整安全审计未完成 |
| 失败停止、重试与回滚规范 | `candidate` | 两类失败的一轮重试已验证，真实回滚、阶段退回和数据补偿未执行 |
| 失败与回滚记录模板 | `candidate` | 失败记录已使用，但回滚路径尚无真实证据 |

这些资产的局部分支可以标注“已取得单项目证据”，但在完整资产层面继续保持 `candidate`。

## 4. 里程碑 B 退出判断

### 已满足

- 风险、边界、权限、证据和人工批准形成可执行闭环；
- Framework 自应用与 YouYu 新任务真实执行均有证据；
- 检查器具有正反例，不是始终成功的形式脚本；
- 失败、唯一一轮修复和复验被连续记录；
- 本地工程通过与生产发布、安全结论保持分离；
- 维护者已接受 B5 有限结论。

### 仍未完成，但不阻止“有限退出”

- 依赖变更；
- OpenAPI、Schema、服务端和客户端完整一致性；
- 真实阶段退回与生产回滚；
- 生产代理、阈值、密钥和发布检查；
- 第二个参考工程与跨项目验证；
- GitHub Billing 与计划额度（维护者明确暂缓，不检查）。

因此建议：

```text
里程碑B：conditional_pass
Harness整体：candidate
指定九项资产：single_project_validated（待维护者批准）
稳定版本：保持v0.1.10
目标版本：保持v0.2.0
里程碑C：不得在批准前启动
```

## 5. 维护者决定

维护者在收到明确的 B6 批准范围后回复“继续呢”。本记录按上下文将其解释为：

1. 接受上述九项资产提升为 `single_project_validated`；
2. 接受其余资产继续保持 `candidate`；
3. 批准里程碑 B 以 `conditional_pass` 有限退出；
4. 允许进入里程碑 C 的正式规划，不直接批量创建 Skills 或 Agents。

## 6. 应用结果

- 九项资产成熟度已按本记录更新；
- Harness 整体仍为 `candidate`；
- 里程碑 B 结果为 `conditional_pass`；
- Framework 稳定版本仍为 `v0.1.10`；
- 里程碑 C 只进入首个 Skill 封装规划。
