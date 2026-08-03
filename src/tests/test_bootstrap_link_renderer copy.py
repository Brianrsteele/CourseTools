import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from documentModels.Link import Link
from rendering.BootStrapLinkRenderer import BootStrapLinkRenderer


class test_bootstrap_section_renderer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document("./link/link-input.md")
        self.target_html_output = self.test_utils.read_test_document(
            "./link/link-output.html"
        )
        self.link = Link(self.markdown_input)
        self.link.set_renderer(BootStrapLinkRenderer(self.link))

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_html_output
        del self.link

    def test_render(self) -> None:
        input = self.link.render()
        output = self.target_html_output
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
