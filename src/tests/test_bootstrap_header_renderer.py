import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from documentModels.DocumentHeader import DocumentHeader
from rendering.BootStrapHeaderRenderer import BootStrapHeaderRenderer


class test_bootstrap_section_renderer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document("./header/header.md")
        self.target_html_output = self.test_utils.read_test_document(
            "./header/bootstrap-header.html"
        )
        self.header = DocumentHeader(self.markdown_input)
        self.bootStrapHeaderRenderer = BootStrapHeaderRenderer(self.header)

    def tearDown(self) -> None:
        del self.bootStrapHeaderRenderer

    def test_render_header(self) -> None:
        self.bootstrap_header = self.bootStrapHeaderRenderer.render_header()
        self.assertEqual(self.bootstrap_header, self.target_html_output)


if __name__ == "__main__":
    unittest.main()
