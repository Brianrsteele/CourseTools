import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from rendering.BootStrapGallerySectionRenderer import BootStrapGallerySectionRenderer
from documentModels.ContentSection import ContentSection


class test_bootstrap_section_renderer(unittest.TestCase):
    # Need to reformat output because visual studio code formats
    # html as it saves it, and the test data in the document
    # gets pretty printed

    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        # test rendering simple student gallery section ----------
        self.markdown_input = self.test_utils.read_test_document(
            "./gallery-section/student-example.md"
        )
        self.target_html_output = self.test_utils.read_test_document(
            "./gallery-section/student-example.html"
        )

        self.markdown_student_gallery_section = ContentSection(self.markdown_input)
        self.markdown_student_gallery_section.set_renderer(
            BootStrapGallerySectionRenderer(self.markdown_student_gallery_section)
        )

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_html_output
        del self.markdown_student_gallery_section

    def test_render(self) -> None:
        # test rendering simple content section ----------------------------
        # need to do some formatting to the rendered text
        input = self.markdown_student_gallery_section.render()
        output = self.target_html_output
        input = self.test_utils.clean_text(input)
        output = self.test_utils.clean_text(output)

        self.test_utils.print_diff(input, output)

        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
