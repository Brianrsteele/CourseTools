import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from documentModels.ContentSection import ContentSection
import tests.TestingUtilities as TestingUtilities
from rendering.BootStrapContentSectionRenderer import BootStrapSectionRenderer


class test_content_section(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document(
            "./content-section/summary.md"
        )
        self.content_only_markdown_input = self.test_utils.read_test_document(
            "./content-section/content.md"
        )
        self.nobold_markdown_input = self.test_utils.read_test_document(
            "./content-section/nobold.md"
        )
        self.target_html_output = self.test_utils.read_test_document(
            "./content-section/bootstrap-summary-render-test.html"
        )
        self.title_only = "Summary"
        self.contentSection = ContentSection(self.markdown_input)

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.content_only_markdown_input
        del self.nobold_markdown_input
        del self.target_html_output
        del self.title_only
        del self.contentSection

    def test_parse_section_title(self) -> None:
        self.assertEqual(self.contentSection.parse_section_title(), self.title_only)

    def test_parse_section_content(self) -> None:
        self.assertEqual(
            self.contentSection.parse_section_content().strip(),
            self.content_only_markdown_input.strip(),
        )

    def test_remove_bold(self) -> None:
        self.assertEqual(
            self.contentSection.remove_bold().strip(),
            self.nobold_markdown_input.strip(),
        )

    def test_set_renderer(self) -> None:
        self.contentSection.set_renderer(BootStrapSectionRenderer(self.contentSection))
        self.assertIsNotNone(self.contentSection.renderer)

    def test_render(self) -> None:
        # self.contentSection.remove_bold()
        self.contentSection.set_renderer(BootStrapSectionRenderer(self.contentSection))
        # Deal with the html formatting that VScode/prettier is applying
        test_output = self.contentSection.render()
        test_output = self.test_utils.clean_text(test_output)

        render_output = self.target_html_output
        render_output = self.test_utils.clean_text(render_output)

        self.assertEqual(test_output, render_output)


if __name__ == "__main__":
    unittest.main()
