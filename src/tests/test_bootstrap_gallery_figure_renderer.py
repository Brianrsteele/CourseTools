import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from documentModels.Image import Image
from documentModels.Figure import Figure

from rendering.BootStrapGalleryFigureRenderer import BootStrapGalleryFigureRenderer


class test_bootstrap_image_renderer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        # set up test for an image with a title
        self.markdown_input = self.test_utils.read_test_document(
            "./figure/image-with-title-figure.md"
        )
        self.target_html_output = self.test_utils.read_test_document(
            "./figure/gallery-image-with-title-figure.html"
        )
        self.gallery_figure = Figure(self.markdown_input)
        self.gallery_figure.set_renderer(
            BootStrapGalleryFigureRenderer(self.gallery_figure)
        )

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_html_output
        del self.gallery_figure

    def test_render_gallery_figure(self) -> None:
        # test a simple figure with a caption and no test
        input = self.gallery_figure.renderer.render()
        output = self.target_html_output

        input = self.test_utils.clean_text(input)
        output = self.test_utils.clean_text(output)

        self.test_utils.print_diff(input, output)

        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
