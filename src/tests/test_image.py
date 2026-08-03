import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from documentModels.Image import Image
import tests.TestingUtilities as TestingUtilities
from rendering.BootStrapImageRenderer import BootStrapImageRenderer


class test_image(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document(
            "./image/single_image.md"
        )
        self.target_alt_text = (
            "Water from a fountain spraying in the air in front of ice."
        )
        self.target_path = "./_images/depth-blur-1.jpg"
        self.image = Image(self.markdown_input)
        self.target_html_ouput = self.test_utils.read_test_document(
            "./image/single_image.html"
        )
        self.image.set_renderer(BootStrapImageRenderer(self.image))

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_alt_text
        del self.target_path
        del self.image
        del self.target_html_ouput

    def test_parse_alt_text(self) -> None:
        self.assertEqual(self.image.parse_alt_text(), self.target_alt_text)

    def test_parse_image_path(self) -> None:
        self.assertEqual(self.image.parse_image_path(), self.target_path)

    def test_set_renderer(self) -> None:
        self.assertIsNotNone(self.image.render)

    def test_renderer(self) -> None:
        markdown_input = self.image.render()
        html_output = self.target_html_ouput
        markdown_input = self.test_utils.clean_text(markdown_input)
        html_output = self.test_utils.clean_text(html_output)
        self.assertEqual(markdown_input, html_output)


if __name__ == "__main__":
    unittest.main()
