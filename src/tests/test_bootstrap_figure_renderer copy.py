import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from documentModels.Image import Image
from documentModels.Figure import Figure
from rendering.BootStrapImageRenderer import BootStrapImageRenderer
from rendering.BootStrapFigureRenderer import BootStrapFigureRenderer


class test_bootstrap_image_renderer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        # set up test for an image with a title
        self.markdown_input = self.test_utils.read_test_document(
            "./figure/image-with-title-figure.md"
        )
        self.target_html_output = self.test_utils.read_test_document(
            "./figure/image-with-title-figure.html"
        )
        self.figure = Figure(self.markdown_input)
        self.figure.set_renderer(BootStrapFigureRenderer(self.figure))

        # set up test for image with title and text (links)
        self.figure_with_text_markdown_input = self.test_utils.read_test_document(
            "./figure/image-with-text-figure.md"
        )
        self.figure_with_text_html_output = self.test_utils.read_test_document(
            "./figure/image-with-text-figure.html"
        )
        self.figure_with_text = Figure(self.figure_with_text_markdown_input)
        self.figure_with_text.set_renderer(
            BootStrapFigureRenderer(self.figure_with_text)
        )

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_html_output

    def test_render_image_with_title(self) -> None:
        # test a simple figure with a caption and no test
        markdown_input = self.figure.renderer.render()
        html_output = self.target_html_output

        markdown_input = self.test_utils.clean_text(markdown_input)
        html_output = self.test_utils.clean_text(html_output)

        self.assertEqual(markdown_input, html_output)

    def test_render_image_with_title_and_text(self) -> None:
        # test a figure that has a caption and text/links
        markdown_input = self.figure_with_text.renderer.render()
        html_output = self.figure_with_text_html_output

        markdown_input = self.test_utils.clean_text(markdown_input)
        html_output = self.test_utils.clean_text(html_output)

        self.assertEqual(markdown_input, html_output)


if __name__ == "__main__":
    unittest.main()
