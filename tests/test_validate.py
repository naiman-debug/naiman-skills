"""Positive and negative fixtures for the repository validator."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate.py"
SPEC = importlib.util.spec_from_file_location("repo_validate", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="naiman-validator-")
        self.root = Path(self.temp.name)
        (self.root / "VERSION").write_text("0.1.0\n", encoding="utf-8")
        self.skill = self.root / "skills" / "sample-skill"
        (self.skill / "agents").mkdir(parents=True)
        self.entry = self.skill / "SKILL.md"
        self.entry.write_text(
            '---\nname: sample-skill\ndescription: 用于示例\nmetadata:\n'
            '  version: "0.1.0"\n---\n正文。\n', encoding="utf-8")
        (self.skill / "README.md").write_text("# 示例\n", encoding="utf-8")
        (self.skill / "agents" / "openai.yaml").write_text(
            'interface:\n  display_name: "示例"\n  short_description: "示例说明"\n'
            '  default_prompt: "Use $sample-skill"\n', encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_complete_package(self):
        self.assertEqual(MODULE.validate(self.root), ([], 1))

    def test_nested_skill_entry_rejected(self):
        ref = self.skill / "references" / "upstream"
        ref.mkdir(parents=True)
        nested = ref / "SKILL.md"
        nested.write_text(self.entry.read_text(encoding="utf-8"), encoding="utf-8")
        self.assertTrue(any("嵌套SKILL.md" in e for e in MODULE.validate(self.root)[0]))
        nested.rename(ref / "UPSTREAM-SKILL.md")
        self.assertEqual(MODULE.validate(self.root), ([], 1))

    def test_https_reference_is_not_a_drive_path(self):
        (self.skill / "README.md").write_text("[资料](https://example.org/guide)", encoding="utf-8")
        self.assertEqual(MODULE.validate(self.root), ([], 1))

    def test_missing_dependency(self):
        content = self.entry.read_text(encoding="utf-8")
        self.entry.write_text(content.replace('  version:', '  requires: "absent-skill"\n  version:'), encoding="utf-8")
        self.assertTrue(any("未打包" in e for e in MODULE.validate(self.root)[0]))

    def test_stale_version(self):
        (self.root / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        self.assertTrue(any("version" in e for e in MODULE.validate(self.root)[0]))

    def test_broken_reference(self):
        (self.skill / "README.md").write_text("[引用](references/missing.md)", encoding="utf-8")
        self.assertTrue(any("不存在" in e for e in MODULE.validate(self.root)[0]))

    def test_path_outside_package(self):
        (self.skill / "README.md").write_text("[引用](../../../../outside.md)", encoding="utf-8")
        self.assertTrue(any("越出仓库" in e for e in MODULE.validate(self.root)[0]))

    def test_author_path_rejected_without_echo(self):
        private_path = "C:" + "\\Users\\someone\\private.md"
        self.entry.write_text(self.entry.read_text(encoding="utf-8") + private_path, encoding="utf-8")
        errors = MODULE.validate(self.root)[0]
        self.assertTrue(any("个人路径" in e for e in errors))
        self.assertFalse(any(private_path in e for e in errors))


if __name__ == "__main__":
    unittest.main()
