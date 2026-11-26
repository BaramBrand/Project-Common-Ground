import tempfile
import unittest
from pathlib import Path

from validate_project_integrity import REQUIRED_FILES, validate_repository


class ProjectIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]

    def test_canonical_governance_and_research_documents_exist(self):
        self.assertEqual(validate_repository(self.root), [])
        self.assertTrue(all((self.root / name).is_file() for name in REQUIRED_FILES))

    def test_missing_required_document_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in REQUIRED_FILES:
                (root / name).write_text("placeholder", encoding="utf-8")
            (root / "SECURITY.md").unlink()
            self.assertTrue(any("missing required document: SECURITY.md" in error for error in validate_repository(root)))

    def test_research_standards_must_keep_evidence_labels_and_alternatives(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in REQUIRED_FILES:
                (root / name).write_text("placeholder", encoding="utf-8")
            (root / "RESEARCH-STANDARDS.md").write_text("no evidence labels", encoding="utf-8")
            errors = validate_repository(root)
            self.assertTrue(any("RESEARCH-STANDARDS.md" in error for error in errors))

    def test_governance_must_keep_human_stewardship_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in REQUIRED_FILES:
                (root / name).write_text("placeholder", encoding="utf-8")
            (root / "GOVERNANCE.md").write_text("decisions only", encoding="utf-8")
            errors = validate_repository(root)
            self.assertTrue(any("GOVERNANCE.md" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
