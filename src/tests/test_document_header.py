import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from documentModels.DocumentHeader import DocumentHeader
import tests.TestingUtilities as TestingUtilities
from rendering.BootStrapHeaderRenderer import BootStrapHeaderRenderer


class test_document_header(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document("./header/header.md")
        self.only_title_markdown_input = self.test_utils.read_test_document(
            "./header/only-title-header.md"
        )
        self.content = "This is a quick note."
        self.author = "Brian Steele"
        self.modfied_date = "3/1/1971"
        self.title = "Depth Blur Project"
        self.target_html_output = self.test_utils.read_test_document(
            "./header/bootstrap-header.html"
        )

        self.header = DocumentHeader(self.markdown_input)
        self.only_title_header = DocumentHeader(self.only_title_markdown_input)

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.content
        del self.author
        del self.modfied_date
        del self.title
        del self.header
        del self.only_title_markdown_input
        del self.only_title_header

    def test_parse_header_title(self) -> None:
        self.assertEqual(self.header.parse_header_title(), self.title)
        # What if there is no content in the header besides teh title...
        self.assertEqual(self.only_title_header.parse_header_title(), self.title)

    def test_parse_header_content(self) -> None:
        self.assertEqual(self.header.parse_header_content(), self.content)
        # What if there is no content in the header besides teh title...
        self.assertEqual(self.only_title_header.parse_header_content(), None)

    def test_parse_author(self) -> None:
        self.assertEqual(self.header.parse_author(), self.author)
        # What if there is no content in the header besides teh title...
        self.assertEqual(self.only_title_header.parse_author(), None)

    def test_parse_modified_date(self) -> None:
        self.assertEqual(self.header.parse_modified_date(), self.modfied_date)
        # What if there is no content in the header besides teh title...
        self.assertEqual(self.only_title_header.parse_modified_date(), None)

    def test_set_renderer(self) -> None:
        self.header.set_renderer(BootStrapHeaderRenderer(self.header))
        self.assertIsInstance(self.header.renderer, BootStrapHeaderRenderer)

    def test_render(self) -> None:
        self.header.set_renderer(BootStrapHeaderRenderer(self.header))
        self.assertEqual(self.header.render(), self.target_html_output)


if __name__ == "__main__":
    unittest.main()
