import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from documentModels.DocumentFooter import DocumentFooter
from rendering.BootStrapFooterRenderer import BootStrapFooterRenderer


class test_bootstrap_section_renderer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document("./footer/footer.md")
        self.target_html_output = self.test_utils.read_test_document(
            "./footer/bootstrap-footer.html"
        )
        self.footer = DocumentFooter(self.markdown_input)
        self.bootstrap_footer_renderer = self.footer.set_renderer(
            BootStrapFooterRenderer(self.footer)
        )
        # test for a footer with no content ------------
        self.footer_no_content_md = ""
        self.footer_no_content_target_html_output = self.test_utils.read_test_document(
            "./footer/bootstrap-footer-no-content.html"
        )
        self.no_content_footer = DocumentFooter(self.footer_no_content_md)
        self.no_content_bootstrap_footer_renderer = self.no_content_footer.set_renderer(
            BootStrapFooterRenderer(self.no_content_footer)
        )

    def tearDown(self) -> None:
        del self.bootstrap_footer_renderer
        del self.test_utils
        del self.markdown_input
        del self.target_html_output
        del self.footer
        del self.footer_no_content_md
        del self.footer_no_content_target_html_output
        del self.no_content_footer
        del self.no_content_bootstrap_footer_renderer

    def test_render_footer(self) -> None:
        # test regular footer with content ------------------------
        footer_output = self.footer.renderer.render_footer()
        target_output = self.target_html_output
        footer_output = self.test_utils.clean_text(footer_output)
        target_output = self.test_utils.clean_text(target_output)
        self.assertEqual(footer_output, target_output)

        # test a footer with no content
        no_content_footer_output = self.no_content_footer.renderer.render_footer()
        no_content_target_ouput = self.footer_no_content_target_html_output
        no_content_footer_output = self.test_utils.clean_text(no_content_footer_output)
        no_content_target_ouput = self.test_utils.clean_text(no_content_target_ouput)
        self.assertEqual(no_content_footer_output, no_content_target_ouput)


if __name__ == "__main__":
    unittest.main()
