import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from documentModels.Link import Link
import tests.TestingUtilities as TestingUtilities


class test_image(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        self.markdown_input = self.test_utils.read_test_document("./link/link-input.md")
        self.target_html_ouput = self.test_utils.read_test_document(
            "./link/link-output.html"
        )
        self.link = Link(self.markdown_input)

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_html_ouput
        del self.link

    def test_parse_url(self) -> None:
        input = self.link.parse_url()
        url_text = "https://cnn.com"
        self.assertEqual(input, url_text)

    def test_parse_link(self) -> None:
        input = self.link.parse_link_text()
        link_text = "A link to CNN"
        self.assertEqual(input, link_text)

    def test_set_renderer(self) -> None:
        pass

    def test_render(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
