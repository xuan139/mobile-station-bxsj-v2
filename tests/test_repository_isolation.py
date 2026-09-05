from pathlib import Path
from unittest import TestCase


ROOT = Path(__file__).resolve().parents[1]


class RepositoryIsolationTests(TestCase):
    def test_source_does_not_import_green_v2(self) -> None:
        for path in (ROOT / "src").rglob("*.py"):
            source = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("import green_v2", source)
            self.assertNotIn("from green_v2", source)

    def test_green_v2_package_is_not_present(self) -> None:
        self.assertFalse((ROOT / "src" / "green_v2").exists())

