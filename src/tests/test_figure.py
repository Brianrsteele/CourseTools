import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from documentModels.Figure import Figure
from documentModels.Image import Image
import tests.TestingUtilities as TestingUtilities


class test_image(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document(
            "./figure/image-with-title-figure.md"
        )
        self.markdown_input_with_text = self.test_utils.read_test_document(
            "./figure/image-with-text-figure.md"
        )
        self.target_html_ouput = self.test_utils.read_test_document(
            "./figure/image-with-title-figure.html"
        )

        # create a mock image object
        self.test_image = Image("![This is a test image.](../_images/test.jpg)")

        # create caption text to test against
        self.test_caption_text = "Student Work. _Untitled Image_. 2024."

        # create figure text to test against
        self.figure_text = """  - [Google Images](http://www.google.com/search?q=Diane+Arbus+photographer&tbm=isch)
  - [Wikipedia](http://en.wikipedia.org/wiki/Diane_Arbus)
  - [Youtube](https://www.youtube.com/watch?v=wKXwCctBLQU)"""

        # create a Figure object from markdown with a single title
        # to test
        self.image_with_title_figure = Figure(self.markdown_input)

        # create a Figure object from markdown with a title and text
        self.image_with_text_figure = Figure(self.markdown_input_with_text)

        # import figure text with hypens
        self.figure_with_hyphen_markdown_input = self.test_utils.read_test_document(
            "./figure/image-with-hypens.md"
        )
        self.figure_with_hyphens = Figure(self.figure_with_hyphen_markdown_input)

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_html_ouput
        del self.test_image
        del self.test_caption_text
        del self.image_with_title_figure

    def test_parse_image(self) -> None:
        # image with just a caption
        self.assertIsNotNone(self.image_with_title_figure.image)
        self.assertEqual(str(self.image_with_title_figure.image), str(self.test_image))
        # image with a caption and text
        self.assertIsNotNone(self.image_with_text_figure.image)
        self.assertEqual(str(self.image_with_text_figure.image), str(self.test_image))

    def test_parse_caption(self) -> None:
        # image with just a caption
        self.assertEqual(self.image_with_title_figure.caption, self.test_caption_text)
        # image with a caption and text
        self.assertEqual(self.image_with_text_figure.caption, self.test_caption_text)

    def test_parse_caption_with_hyphens(self) -> None:
        figure_input = self.figure_with_hyphens.caption
        figure_output = self.test_caption_text
        figure_input = self.test_utils.clean_text(figure_input)
        figure_output = self.test_utils.clean_text(figure_output)
        self.assertEqual(figure_input, figure_output)

    def test_parse_text(self) -> None:
        input_markdown = self.image_with_text_figure.text
        test_markdown = self.figure_text
        # clean up the text for easier comparison
        input_markdown = self.test_utils.clean_text(input_markdown)
        test_markdown = self.test_utils.clean_text(test_markdown)
        self.assertEqual(input_markdown, test_markdown)

        # A figure without text should return None for the text
        self.assertEqual(self.image_with_title_figure.text, None)

    def test_parse_text_with_hyphens(self) -> None:
        input = self.figure_with_hyphens.text
        output = None

        self.assertEquals(input, output)

    def test_set_renderer(self) -> None:
        pass

    def test_render(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
