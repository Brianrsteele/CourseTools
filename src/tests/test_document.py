import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from documentModels.Document import Document
from documentModels.DocumentHeader import DocumentHeader
from documentModels.DocumentFooter import DocumentFooter
from documentModels.ContentSection import ContentSection
import tests.TestingUtilities as TestingUtilities


class test_document_(unittest.TestCase):
    def setUp(self) -> None:
        # add some useful utilities
        self.test_utils = TestingUtilities
        # open a markdown example file for a single section document ----------------------------------------
        self.markdown_input = self.test_utils.read_test_document(
            "./document/one-section-project.md"
        )
        # create a document to test
        self.document = Document(self.markdown_input)
        # create fake header markdown to test against.
        self.header_markdown_input = "# Depth Blur Project\n\nAuthor: Brian Steele\nModified Date: 3/1/1971\n\nThis is some header content."
        self.documentHeader = DocumentHeader(self.header_markdown_input)
        # create fake footer markdown to test against.
        self.footer_markdown_input = "This is some footer content."
        self.documentFooter = DocumentFooter(self.footer_markdown_input)
        # create fake markdown content to test.
        self.single_summary_section_markdown_input = "Summary\n\n"
        self.single_summary_section_markdown_input += (
            "Turn in four (4) images in the JPEG file format and a link "
        )
        self.single_summary_section_markdown_input += "to a Lightroom album with one hundred (100) images taken for this project.\n\n"
        self.single_summary_section_markdown_input += (
            "- You can photograph anything you want.\n"
        )
        self.single_summary_section_markdown_input += (
            "- One (1) image should demonstrate **fozen motion**.\n"
        )
        self.single_summary_section_markdown_input += (
            "- One (1) image should demonstrate **blurred motion**.\n"
        )
        self.single_summary_section_markdown_input += (
            "- One (1) image should demonstrate **large depth of field**.\n"
        )
        self.single_summary_section_markdown_input += (
            "- One (1) image should demonstrate **shallow depth of field**.\n"
        )
        self.single_summary_section_markdown_input += (
            "- We will look at the images you submit in this week's "
        )
        self.single_summary_section_markdown_input += (
            "discussion for online students and in class for in-person students."
        )
        # create a list of ContentSection objects
        self.single_summary_section_list = []
        content_section = ContentSection(self.single_summary_section_markdown_input)
        self.single_summary_section_list.append(content_section)
        self.document.append_section(self.single_summary_section_markdown_input)
        # need a new document to test parse_document
        self.document2 = Document(self.markdown_input)
        # import the html output to test render()
        self.one_section_bootstrap_output = self.test_utils.read_test_document(
            "./document/one-section-project.html"
        )

        # open a markdown document for a three section document ------------------------
        self.three_section_raw_content = self.test_utils.read_test_document(
            "./document/three-section-project.md"
        )
        # create a three section document to test
        self.three_section_document = Document(self.three_section_raw_content)
        # open target html to test for three section document
        self.three_section_target = self.test_utils.read_test_document(
            "./document/three-section-project.html"
        )

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.document
        del self.header_markdown_input
        del self.footer_markdown_input
        del self.documentHeader
        del self.documentFooter
        del self.single_summary_section_markdown_input
        del self.single_summary_section_list
        del self.document2
        del self.one_section_bootstrap_output
        del self.three_section_raw_content
        del self.three_section_document
        del self.three_section_target

    def test_parse_document(self) -> None:
        self.document2.parse_document()
        self.assertIsNot("", self.document2.header)
        self.assertEqual(self.document2.header.title, self.documentHeader.title)
        self.assertEqual(self.document2.header.content, self.documentHeader.content)
        self.assertEqual(self.document2.header.author, self.documentHeader.author)
        self.assertEqual(
            self.document2.header.modified_date, self.documentHeader.modified_date
        )
        self.assertEqual(self.document2.footer.content, self.documentFooter.content)
        self.assertEqual(
            str(self.document2.sections[0]),
            str(self.single_summary_section_list[0]),
        )

    def test_parse_all_sections(self) -> None:
        self.assertEqual(
            self.document.parse_all_sections_text()[0],
            self.single_summary_section_markdown_input,
        )

    def test_add_header(self) -> None:
        self.document.add_header()
        self.assertEqual(self.document.header.title, self.documentHeader.title)
        self.assertEqual(self.document.header.author, self.documentHeader.author)
        self.assertEqual(
            self.document.header.modified_date, self.documentHeader.modified_date
        )
        self.assertEqual(self.document.header.content, self.documentHeader.content)
        self.assertEqual(str(self.document.header), str(self.documentHeader))

    def test_parse_header(self) -> None:
        # uses the self.raw_content markdown text to find and return
        # the markdown content to create a header.
        self.assertEqual(self.document.parse_header(), self.header_markdown_input)

    def test_add_footer(self) -> None:
        self.document.add_footer()
        self.assertEqual(self.document.footer.content, self.documentFooter.content)
        self.assertEqual(str(self.document.footer), str(self.documentFooter))

    def test_parse_footer(self) -> None:
        # uses the self.raw_content markdown text to find and return
        # the markdown content to create a footer.
        self.assertEqual(self.document.parse_footer(), self.footer_markdown_input)

    def test_append_section(self):
        self.assertEqual(
            self.document.sections[0].title,
            self.single_summary_section_list[0].title,
        )
        self.assertEqual(
            self.document.sections[0].content,
            self.single_summary_section_list[0].content,
        )
        self.assertEqual(
            str(self.document.sections[0]), str(self.single_summary_section_list[0])
        )

    def test_render_document(self):
        # test one section document
        self.document2.parse_document()
        output = self.document2.render_document("bootstrap")
        target_output = self.one_section_bootstrap_output
        output = self.test_utils.clean_text(output)
        target_output = self.test_utils.clean_text(target_output)
        self.assertEqual(
            output,
            target_output,
        )

        # test three section document -----------------------------------------------------
        self.three_section_document.parse_document()
        three_section_output = self.three_section_document.render_document("bootstrap")
        three_section_target_output = self.three_section_target
        three_section_output = self.test_utils.clean_text(three_section_output)
        three_section_target_output = self.test_utils.clean_text(
            three_section_target_output
        )
        self.assertEqual(three_section_output, three_section_target_output)


if __name__ == "__main__":
    unittest.main()
