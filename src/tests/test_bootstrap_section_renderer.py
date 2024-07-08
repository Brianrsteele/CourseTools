import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from rendering.BootStrapContentSectionRenderer import BootStrapSectionRenderer
from documentModels.ContentSection import ContentSection


class test_bootstrap_section_renderer(unittest.TestCase):
    # Need to reformat output because visual studio code formats
    # html as it saves it, and the test data in the document
    # gets pretty printed

    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        # test rendering simple content section ----------
        self.markdown_input = self.test_utils.read_test_document(
            "./content-section/depth-blur-summary-content.md"
        )
        self.title_only = "Summary"
        self.target_html_output = self.test_utils.read_test_document(
            "./content-section/bootstrap-summary.html"
        )
        self.bootstrapRenderer = BootStrapSectionRenderer(
            self.title_only, self.markdown_input
        )
        # test rendering a content section with a table---------
        self.table_content_markdown_input = self.test_utils.read_test_document(
            "./content-section/content_section_with_table.md"
        )
        self.table_content_target_html_output = self.test_utils.read_test_document(
            "./content-section/content_section_with_table.html"
        )
        self.table_content_section = ContentSection(self.table_content_markdown_input)
        self.table_content_section.parse_section_content()
        self.table_content_section.parse_section_title()
        self.table_content_section.set_renderer(
            BootStrapSectionRenderer(
                self.table_content_section.title, self.table_content_section.content
            )
        )

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.title_only
        del self.target_html_output
        del self.bootstrapRenderer
        del self.table_content_markdown_input
        del self.table_content_target_html_output
        del self.table_content_section

    def test_render_section(self) -> None:
        # test rendering simple content section ----------------------------
        # need to do some formatting to the rendered text
        bootstrap_section = self.bootstrapRenderer.render_section()
        bootstrap_section = self.test_utils.clean_text(bootstrap_section)

        # need to do some formatting to the test text
        target_output = self.target_html_output
        target_output = self.test_utils.clean_text(target_output)

        self.assertEqual(bootstrap_section, target_output)

        # test rendering content section with a table -----------------------
        bootstrap_table_output = self.table_content_section.renderer.render_section()
        bootstrap_table_output = self.test_utils.clean_text(bootstrap_table_output)
        target_table_output = self.table_content_target_html_output
        target_table_output = self.test_utils.clean_text(target_table_output)

        self.test_utils.print_diff(bootstrap_table_output, target_table_output)

        self.assertEqual(bootstrap_table_output, target_table_output)


if __name__ == "__main__":
    unittest.main()
