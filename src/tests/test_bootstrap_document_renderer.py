import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from documentModels.Document import Document
from rendering.BootStrapDocumentRenderer import BootStrapDocumentRenderer


class test_bootstrap_document_renderer(unittest.TestCase):
    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        # import materials for a one section document
        self.one_section_markdown_input = self.test_utils.read_test_document(
            "./document/one-section-project.md"
        )
        self.one_section_target_html_output = self.test_utils.read_test_document(
            "./document/one-section-project.html"
        )
        self.one_section_document = Document(self.one_section_markdown_input)
        self.one_section_document.set_renderer(
            BootStrapDocumentRenderer(self.one_section_document)
        )

        # import materials for a three section document
        self.three_section_markdown_input = self.test_utils.read_test_document(
            "./document/three-section-project.md"
        )
        self.three_section_target_html_output = self.test_utils.read_test_document(
            "./document/three-section-project.html"
        )
        self.three_section_document = Document(self.three_section_markdown_input)
        self.three_section_document.set_renderer(
            BootStrapDocumentRenderer(self.three_section_document)
        )

        # import materials for a document with single images
        self.single_image_section_markdown_input = self.test_utils.read_test_document(
            "./document/three-section-project-single-images.md"
        )
        self.single_image_section_target_html_output = (
            self.test_utils.read_test_document(
                "./document/three-section-project-single-images.html"
            )
        )
        self.single_image_section_document = Document(
            self.single_image_section_markdown_input
        )
        self.single_image_section_document.set_renderer(
            BootStrapDocumentRenderer(self.single_image_section_document)
        )

        # import materials for a document with a table
        self.three_section_project_table_markdown_input = (
            self.test_utils.read_test_document(
                "./document/three-section-project-tables.md"
            )
        )

        self.three_section_project_table_html_output = (
            self.test_utils.read_test_document(
                "./document/three-section-project-tables.html"
            )
        )

        self.three_section_project_table_document = Document(
            self.three_section_project_table_markdown_input
        )

    def tearDown(self) -> None:
        del self.test_utils
        del self.one_section_markdown_input
        del self.one_section_target_html_output
        del self.three_section_markdown_input
        del self.three_section_target_html_output
        del self.three_section_document
        del self.single_image_section_markdown_input
        del self.single_image_section_target_html_output
        del self.single_image_section_document

    def test_render_one_section_document(self) -> None:
        # test a simple document
        one_section_input = self.one_section_document.render("Bootstrap")
        one_section_output = self.one_section_target_html_output
        one_section_input = self.test_utils.clean_text(one_section_input)
        one_section_output = self.test_utils.clean_text(one_section_output)
        self.assertEqual(one_section_input, one_section_output)

    def test_render_three_section_document(self) -> None:
        # test a three section document
        three_section_input = self.three_section_document.render("Bootstrap")
        three_section_output = self.three_section_target_html_output
        three_section_input = self.test_utils.clean_text(three_section_input)
        three_section_output = self.test_utils.clean_text(three_section_output)
        self.assertEqual(three_section_input, three_section_output)

    def test_render_document_with_image(self) -> None:
        # test a document with single images without titles
        single_image_section_input = self.single_image_section_document.render(
            "Bootstrap"
        )
        single_image_section_output = self.single_image_section_target_html_output
        single_image_section_input = self.test_utils.clean_text(
            single_image_section_input
        )
        single_image_section_output = self.test_utils.clean_text(
            single_image_section_output
        )
        self.assertEqual(single_image_section_input, single_image_section_output)

    def test_render_document_with_table(self) -> None:
        # test rendering a document with a table in a section
        three_section_project_table_input = (
            self.three_section_project_table_document.render("Bootstrap")
        )
        three_section_project_table_output = (
            self.three_section_project_table_html_output
        )

        three_section_project_table_input = self.test_utils.clean_text(
            three_section_project_table_input
        )

        three_section_project_table_output = self.test_utils.clean_text(
            three_section_project_table_output
        )

        self.assertEqual(
            three_section_project_table_input, three_section_project_table_output
        )


if __name__ == "__main__":
    unittest.main()
