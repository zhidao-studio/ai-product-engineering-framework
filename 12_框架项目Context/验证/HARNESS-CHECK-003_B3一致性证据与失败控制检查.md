# HARNESS-CHECK-003：B3 一致性、证据与失败控制检查

```yaml
check_id: HARNESS-CHECK-003
status: passed
project: AI Product Engineering Framework
milestone: B / Harness 可执行化
work_segment: B3 / 一致性证据与失败控制
baseline_commit: 583549b75e73db9fa97e1925db958fdbfc6fcce5
implementation_commit: fd6095d46a4abacc7721a6069aeab73aee20c9fd
stable_release: v0.1.10
target_release: v0.2.0
verified_at: 2026-07-23
verifier: Codex
reference_validation: not_executed
asset_maturity: candidate
```

## 1. 检查范围

- OpenAPI、Schema、服务端、客户端与错误码一致性；
- 权限、密钥、日志、环境和 Git 历史敏感信息边界；
- 静态、运行、用户和发布证据及结论边界；
- 失败分类、重试上限、停止、退回和回滚；
- 候选模板、机器证据清单和确定性检查脚本。

机器证据清单见 [HARNESS-CHECK-003 JSON](HARNESS-CHECK-003_B3一致性证据与失败控制检查.json)。

## 2. 实际结果

| 检查 | 结果 | 证据 |
|---|---|---|
| Python 单元测试 | 18 项通过 | 两个候选检查器的正反例 |
| 证据模板结构 | 通过 | 三层 `not_executed` 模板没有被误写成通过 |
| Framework 工作区边界 | 13 个改动路径通过 | TASK-027 真实控制清单 |
| Markdown 本地链接 | 9 个变更文件、27 个链接通过 | 本地链接检查 |
| 发布状态一致性 | 通过 | `scripts/check-release-state.sh` |
| 空白和补丁检查 | 通过 | `git diff --check` |
| YouYu 新任务验证 | 未执行 | B4 正式选择参考任务 |

## 3. 反向检查和修复

第一次检查没有通过，发现两个实际问题：

1. 证据模板声明 `static`、`runtime`、`user` 为必需层，却只登记一项静态证据；
2. TASK-027 只允许修改 `08_模板资产/Harness/`，但实现顺手更新了 `08_模板资产/README.md`。

处理结果：

- 补齐运行和用户层未执行证据，模板继续保持 `not_executed`；
- 撤回模板总目录修改，不扩大任务边界；
- 重新执行后，证据模板检查和 13 个实际路径检查通过。

这证明证据检查可以阻止“声明三层、实际只有一层”，任务边界也能阻止无关状态同步。

## 4. 证据边界

- 已证明：候选规则、模板和脚本在 Framework 自应用范围内结构一致；
- 已证明：必需证据未通过时，机器清单不能汇总为 `passed`；
- 未证明：OpenAPI、Schema 和客户端真实一致性；
- 未证明：安全扫描或回滚在真实工程中有效；
- 未证明：用户证据能够减少 YouYu 交付偏差；
- 所有 B3 新资产成熟度继续为 `candidate`。

## 5. 结论

`passed`（仅限 B3 工程和 Framework 自应用范围）。B1 至 B3 的候选控制已经具备，下一步必须进入 YouYu 新任务参考验证准备，不能继续只靠 Framework 自证。
