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
        self.raw_content = self.test_utils.read_test_document("summary.md")
        self.content = self.test_utils.read_test_document("content.md")
        self.nobold = self.test_utils.read_test_document("nobold.md")
        self.render_output = self.test_utils.read_test_document(
            "bootstrap-summary-render-test.html"
        )

        self.title = "Summary"

        self.contentSection = ContentSection(self.raw_content)

    def tearDown(self) -> None:
        del self.contentSection
        del self.content
        del self.title
        del self.raw_content

    def test_parse_section_title(self) -> None:
        self.assertEqual(self.contentSection.parse_section_title(), self.title)

    def test_parse_section_content(self) -> None:
        self.assertEqual(
            self.contentSection.parse_section_content().strip(), self.content.strip()
        )

    def test_remove_bold(self) -> None:
        self.assertEqual(self.contentSection.remove_bold().strip(), self.nobold.strip())

    def test_set_renderer(self) -> None:
        self.contentSection.set_renderer(
            BootStrapSectionRenderer(
                self.contentSection.title, self.contentSection.content
            )
        )
        self.assertIsNotNone(self.contentSection.renderer)

    def test_render(self) -> None:
        # self.contentSection.remove_bold()
        self.contentSection.set_renderer(
            BootStrapSectionRenderer(
                self.contentSection.title, self.contentSection.content
            )
        )
        # Deal with the html formatting that VScode/prettier is applying
        test_output = self.contentSection.render()
        test_output = self.test_utils.clean_text(test_output)

        render_output = self.render_output
        render_output = self.test_utils.clean_text(render_output)

        self.assertEqual(test_output, render_output)


if __name__ == "__main__":
    unittest.main()
