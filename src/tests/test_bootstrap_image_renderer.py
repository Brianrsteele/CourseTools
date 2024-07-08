import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from documentModels.Image import Image
from rendering.BootStrapImageRenderer import BootStrapImageRenderer


class test_bootstrap_image_renderer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document(
            "./image/single_image.md"
        )
        self.target_html_output = self.test_utils.read_test_document(
            "./image/single_image.html"
        )
        self.image = Image(self.markdown_input)
        self.image.set_renderer(BootStrapImageRenderer(self.image))

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_html_output
        del self.image

    def test_render_image(self) -> None:
        input = self.image.renderer.render_image()
        output = self.target_html_output

        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
