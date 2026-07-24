# SKILL-SELF-CHECK-001：受控任务验证 Skill 候选包自应用

```yaml
check_id: SKILL-SELF-CHECK-001
task_id: TASK-20260724-032
status: conditional_pass
milestone: C / Skills、Agents 与 Loop
work_segment: C2 / 首个Skill候选包实现与自应用
framework_release: v0.1.10
target_release: v0.2.0
baseline_commit: 0f7bc520ac6b7a17b227e05a28cf63cb74a41693
skill_commit: 7bf95b6795f7b334ac7fe8c788addecfd443c14f
verified_at: 2026-07-24
verifier: Codex
asset_maturity: candidate
youyu_reference_validation: not_started
```

## 1. 结论

`controlled-task-validation` 候选包已创建并完成 Framework 首次自应用：

```text
读取 TASK-032 Context 与控制清单
→ 使用 range 检查 C2 授权基线到 Skill 提交
→ 检查证据清单结构
→ 人工复核有限结论
→ 输出 conditional_pass
```

候选包可以装配项目内已验证的边界和证据检查器；当前只证明 Framework 自应用，不证明 YouYu 新任务、跨项目、用户验收或生产发布。

## 2. 实际结果

| 检查 | 实际结果 |
|---|---|
| 官方初始化 | 目录和 `SKILL.md` 模板成功创建；首次界面短描述长度检查失败 |
| 元数据生成 | 改用 25–64 字符描述后生成 `agents/openai.yaml` |
| 官方结构验证 | `Skill is valid!` |
| Skill 体积 | `SKILL.md` 105 行，小于 500 行 |
| 候选包文件 | 仅 `SKILL.md` 与 `agents/openai.yaml` |
| 历史范围边界 | `0f7bc520..7bf95b6` 共 12 个路径通过 |
| Harness 检查器测试 | 18 项通过 |
| Framework 状态一致性 | Framework v0.1.10、YouYu v0.1.4、目标 v0.2.0 通过 |
| 证据清单 | 4 项结构与有限结论通过 |
| YouYu 新任务 | 未开始 |
| 发布检查 | 未执行 |

## 3. 首次失败和修正

### 3.1 界面短描述过短

首次初始化使用 20 字符短描述，官方工具要求 25–64 字符，因此只创建了目录和 `SKILL.md`，没有生成 `openai.yaml`。

修正：

- 保留已初始化目录；
- 完成正式 `SKILL.md`；
- 使用合规短描述单独生成 `openai.yaml`；
- 重新执行官方结构验证。

### 3.2 默认 Python 缺少 PyYAML

系统默认 Python 运行 `quick_validate.py` 时缺少 `yaml` 模块。仓库没有因此新增依赖；改用本机已有 PyYAML 6.0 的 Python 3.9 完成官方验证。

这说明 Skill 验证工具依赖需要在执行环境中显式确认，不能把“脚本存在”当成“默认解释器可运行”。

## 4. Skill 标准输出

```yaml
skill: controlled-task-validation
task_id: TASK-20260724-032
repository: zhidao-studio/ai-product-engineering-framework
mode: range
risk_level: medium
task_context_status: active
boundary_check:
  status: passed
  command: check_task_boundary.py --mode range --base 0f7bc520 --head 7bf95b6
  exit_code: 0
  evidence: 12个路径通过
evidence_manifest_check:
  status: passed
  command: check_evidence_manifest.py --manifest TASK-20260724-032_验证证据清单.json
  exit_code: 0
  evidence: 4项证据结构通过
human_review_required: true
human_review_reasons:
  - 是否进入YouYu新任务参考验证
overall_result: conditional_pass
unverified_scopes:
  - YouYu新任务真实验证
  - 跨项目验证
  - 用户验收
  - 生产发布
context_updates:
  - TASK-032
  - C2阶段Context
  - Framework项目Context
```

## 5. 人工语义复核

- Skill 没有复制 Harness 规则、模板或脚本；
- Skill 没有批准高风险变更；
- `range` 边界通过只证明 Git 路径符合 TASK-032；
- 证据清单通过只证明结构和结论没有矛盾；
- `conditional_pass` 不等于候选包已被 YouYu 或其他项目验证；
- 候选包成熟度继续为 `candidate`。

## 6. YouYu 参考验证准备

下一步应在 YouYu 选择一个新的、范围有限且不涉及生产发布的维护任务：

- 已有当前任务 Context；
- 可以建立任务控制清单和验证证据清单；
- 至少执行静态和运行验证；
- 用户可见时增加用户证据；
- 记录 Skill 的触发准确性、误报、人工修正次数和时间成本；
- 不选择 GitHub Billing 与计划额度检查。

未选择具体 YouYu 任务前，不创建空任务或宣称参考验证已经开始。

## 7. 最终边界

Framework 自应用结果：`conditional_pass`。

```text
Skill候选包：已创建
官方结构验证：通过
Framework自应用：通过有限范围
YouYu参考验证：not_started
跨项目验证：not_started
生产发布：not_executed
资产成熟度：candidate
```
