import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "check_task_boundary.py"
SPEC = importlib.util.spec_from_file_location("check_task_boundary", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def manifest(**overrides):
    value = {
        "allowed_paths": ["src/", "README.md", "pom.xml"],
        "forbidden_paths": ["src/secret/", "LICENSE"],
        "high_risk_paths": ["**/*.sql", "src/security/", "pom.xml"],
        "approved_high_risk_paths": [],
        "dependency_files": ["pom.xml", "**/pom.xml"],
        "approved_dependency_files": [],
    }
    value.update(overrides)
    return value


class BoundaryTests(unittest.TestCase):
    def test_allowed_path_passes(self):
        self.assertEqual(MODULE.evaluate_paths(["src/app.py"], manifest()), [])

    def test_outside_allowed_path_fails(self):
        self.assertEqual(
            MODULE.evaluate_paths(["docs/new.md"], manifest()),
            ["超出允许范围: docs/new.md"],
        )

    def test_forbidden_path_wins(self):
        self.assertEqual(
            MODULE.evaluate_paths(["src/secret/key.txt"], manifest()),
            ["禁止修改: src/secret/key.txt"],
        )

    def test_high_risk_requires_approval(self):
        self.assertEqual(
            MODULE.evaluate_paths(["src/security/auth.py"], manifest()),
            ["高风险路径未授权: src/security/auth.py"],
        )

    def test_high_risk_approval_passes(self):
        value = manifest(approved_high_risk_paths=["src/security/"])
        self.assertEqual(MODULE.evaluate_paths(["src/security/auth.py"], value), [])

    def test_dependency_requires_both_approvals(self):
        self.assertEqual(
            MODULE.evaluate_paths(["pom.xml"], manifest()),
            ["高风险路径未授权: pom.xml", "依赖文件未授权: pom.xml"],
        )

    def test_dependency_with_both_approvals_passes(self):
        value = manifest(
            approved_high_risk_paths=["pom.xml"],
            approved_dependency_files=["pom.xml"],
        )
        self.assertEqual(MODULE.evaluate_paths(["pom.xml"], value), [])

    def test_glob_matches_nested_sql(self):
        value = manifest(
            allowed_paths=["db/"], approved_high_risk_paths=["**/*.sql"]
        )
        self.assertEqual(MODULE.evaluate_paths(["db/migration/v1.sql"], value), [])

    def test_double_star_glob_also_matches_root_file(self):
        value = manifest(
            allowed_paths=["schema.sql"], approved_high_risk_paths=["**/*.sql"]
        )
        self.assertEqual(MODULE.evaluate_paths(["schema.sql"], value), [])


if __name__ == "__main__":
    unittest.main()
