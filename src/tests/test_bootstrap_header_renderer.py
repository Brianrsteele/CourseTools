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
        self.output = self.test_utils.read_test_document("bootstrap-header.html")
        self.input = self.test_utils.read_test_document("header.md")
        self.header = DocumentHeader(self.input)
        self.bootStrapHeaderRenderer = BootStrapHeaderRenderer(self.header)

    def tearDown(self) -> None:
        del self.bootStrapHeaderRenderer

    def test_render_header(self) -> None:
        self.bootstrap_header = self.bootStrapHeaderRenderer.render_header()
        self.assertEqual(self.bootstrap_header, self.output)


if __name__ == "__main__":
    unittest.main()
