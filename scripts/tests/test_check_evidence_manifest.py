import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "check_evidence_manifest.py"
SPEC = importlib.util.spec_from_file_location("check_evidence_manifest", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def evidence(
    evidence_id,
    layer,
    *,
    required=True,
    status="passed",
    executed=True,
):
    return {
        "id": evidence_id,
        "layer": layer,
        "assertion": f"{layer} assertion",
        "required": required,
        "status": status,
        "executed": executed,
        "step": "run check" if executed else "",
        "exit_code": 0 if executed else None,
        "result_summary": "passed" if executed else "",
        "evidence_path": "evidence/result.txt" if executed else "",
        "actor": "tester" if executed else "",
        "executed_at": "2026-07-23T12:00:00+08:00" if executed else "",
    }


def manifest(**overrides):
    value = {
        "manifest_version": "0.1",
        "task_id": "TASK-TEST-001",
        "repository": "owner/repo",
        "baseline_commit": "abc123",
        "risk_level": "medium",
        "overall_result": "passed",
        "formal_business_validation": "passed",
        "required_layers": ["static", "runtime", "user"],
        "evidence": [
            evidence("S-001", "static"),
            evidence("R-001", "runtime"),
            evidence("U-001", "user"),
        ],
    }
    value.update(overrides)
    return value


class EvidenceManifestTests(unittest.TestCase):
    def test_valid_formal_business_evidence_passes(self):
        self.assertEqual(MODULE.validate_manifest(manifest()), [])

    def test_passed_overall_rejects_unexecuted_required_evidence(self):
        value = manifest(
            evidence=[
                evidence("S-001", "static"),
                evidence(
                    "R-001",
                    "runtime",
                    status="not_executed",
                    executed=False,
                ),
                evidence("U-001", "user"),
            ]
        )
        problems = MODULE.validate_manifest(value)
        self.assertTrue(
            any("必需证据未通过: R-001" in problem for problem in problems)
        )

    def test_formal_pass_requires_user_layer(self):
        value = manifest(
            required_layers=["static", "runtime"],
            evidence=[
                evidence("S-001", "static"),
                evidence("R-001", "runtime"),
            ],
        )
        problems = MODULE.validate_manifest(value)
        self.assertIn("正式业务通过缺少 user 层必需通过证据", problems)

    def test_passed_evidence_must_be_executed(self):
        value = manifest(
            overall_result="conditional_pass",
            formal_business_validation="not_executed",
            required_layers=["static"],
            evidence=[
                evidence(
                    "S-001",
                    "static",
                    status="passed",
                    executed=False,
                )
            ],
        )
        problems = MODULE.validate_manifest(value)
        self.assertTrue(any("executed 必须为 true" in problem for problem in problems))

    def test_executed_evidence_requires_provenance(self):
        item = evidence("S-001", "static")
        item["evidence_path"] = ""
        value = manifest(
            overall_result="conditional_pass",
            formal_business_validation="not_executed",
            required_layers=["static"],
            evidence=[item],
        )
        problems = MODULE.validate_manifest(value)
        self.assertIn("evidence[0].evidence_path 在已执行时不能为空", problems)

    def test_duplicate_evidence_ids_fail(self):
        value = manifest(
            overall_result="conditional_pass",
            formal_business_validation="not_executed",
            required_layers=["static", "runtime"],
            evidence=[
                evidence("E-001", "static"),
                evidence("E-001", "runtime"),
            ],
        )
        self.assertIn("证据编号重复: E-001", MODULE.validate_manifest(value))

    def test_required_layer_needs_required_evidence(self):
        value = manifest(
            overall_result="conditional_pass",
            formal_business_validation="not_executed",
            required_layers=["static", "runtime"],
            evidence=[
                evidence("S-001", "static"),
                evidence("R-001", "runtime", required=False),
            ],
        )
        problems = MODULE.validate_manifest(value)
        self.assertIn("required_layers 声明 runtime，但没有该层必需证据", problems)

    def test_failed_overall_needs_failed_required_evidence(self):
        value = manifest(
            overall_result="failed",
            formal_business_validation="failed",
            required_layers=["static"],
            evidence=[evidence("S-001", "static")],
        )
        problems = MODULE.validate_manifest(value)
        self.assertIn("overall_result=failed 但没有必需证据标记为 failed", problems)

    def test_not_executed_template_is_valid(self):
        value = manifest(
            overall_result="not_executed",
            formal_business_validation="not_executed",
            required_layers=["static"],
            evidence=[
                evidence(
                    "S-001",
                    "static",
                    status="not_executed",
                    executed=False,
                )
            ],
        )
        self.assertEqual(MODULE.validate_manifest(value), [])


if __name__ == "__main__":
    unittest.main()
