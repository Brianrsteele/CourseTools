import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from documentModels.DocumentFooter import DocumentFooter
import tests.TestingUtilities as TestingUtilities


class test_document_footer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document("./footer/footer.md")
        self.footer = DocumentFooter(self.markdown_input)
        self.content = "This is some footer content."
        self.has_no_content = DocumentFooter("")

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.footer
        del self.content
        del self.has_no_content

    def test_parse_footer_content(self) -> None:
        self.assertEqual(self.footer.parse_footer_content(), self.content)
        self.assertEqual(self.has_no_content.parse_footer_content(), None)


if __name__ == "__main__":
    unittest.main()
