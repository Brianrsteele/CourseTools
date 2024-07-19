import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import tests.TestingUtilities as TestingUtilities
from rendering.BootStrapSectionRenderer import BootStrapSectionRenderer
from documentModels.ContentSection import ContentSection


class test_bootstrap_section_renderer(unittest.TestCase):
    # Need to reformat output because visual studio code formats
    # html as it saves it, and the test data in the document
    # gets pretty printed

    def setUp(self) -> None:
        self.test_utils = TestingUtilities
        # test rendering simple content section ----------
        self.markdown_input = self.test_utils.read_test_document(
            "./content-section/depth-blur-summary-content.md"
        )
        self.markdown_content_section = ContentSection(self.markdown_input)
        self.target_html_output = self.test_utils.read_test_document(
            "./content-section/bootstrap-summary.html"
        )
        self.bootstrapRenderer = BootStrapSectionRenderer(self.markdown_content_section)

        # test rendering a content section with a table---------
        self.table_content_markdown_input = self.test_utils.read_test_document(
            "./content-section/content_section_with_table.md"
        )
        self.table_content_target_html_output = self.test_utils.read_test_document(
            "./content-section/content_section_with_table.html"
        )
        self.table_content_section = ContentSection(self.table_content_markdown_input)
        self.table_content_section.parse_section_content()
        self.table_content_section.parse_section_title()
        self.table_content_section.set_renderer(
            BootStrapSectionRenderer(self.table_content_section)
        )

        # test rendering a content section with images with no captions ---------------
        self.single_image_section_markdown_input = self.test_utils.read_test_document(
            "./content-section/single-image-section-no-caption.md"
        )
        self.single_image_section_target_html_output = (
            self.test_utils.read_test_document(
                "./content-section/single-image-section-no-caption.html"
            )
        )
        self.single_image_content_section = ContentSection(
            self.single_image_section_markdown_input
        )
        self.single_image_content_section.set_renderer(
            BootStrapSectionRenderer(self.single_image_content_section)
        )

        # test rendering a content section with a single figure with a caption
        self.single_figure_caption_markdown_input = self.test_utils.read_test_document(
            "./content-section/single-figure.md"
        )

        self.single_figure_caption_html_output = self.test_utils.read_test_document(
            "./content-section/single-figure.html"
        )

        self.single_figure_content_section = ContentSection(
            self.single_figure_caption_markdown_input
        )

        self.single_figure_bootstrap_renderer = (
            self.single_figure_content_section.set_renderer(
                BootStrapSectionRenderer(self.single_figure_content_section)
            )
        )

        # test rendering a content section with a figure that has links
        self.single_figure_links_markdown_input = self.test_utils.read_test_document(
            "./content-section/single-figure-content-section-links.md"
        )
        self.single_figure_links_html_output = self.test_utils.read_test_document(
            "./content-section/single-figure-content-section-links.html"
        )
        self.single_figure_links_content_section = ContentSection(
            self.single_figure_links_markdown_input
        )
        self.single_figure_links_content_section.set_renderer(
            BootStrapSectionRenderer(self.single_figure_links_content_section)
        )

        # test rendering a content section that has three figures with captions
        self.three_figures_with_captions_markdown_input = (
            self.test_utils.read_test_document(
                "./content-section/three-figure-captions.md"
            )
        )
        self.three_figures_with_captions_html_output = (
            self.test_utils.read_test_document(
                "./content-section/three-figure-captions.html"
            )
        )
        self.three_figures_with_captions_content_sections = ContentSection(
            self.three_figures_with_captions_markdown_input
        )
        self.three_figures_with_captions_content_sections.set_renderer(
            BootStrapSectionRenderer(self.three_figures_with_captions_content_sections)
        )

    def tearDown(self) -> None:
        del self.test_utils
        del self.markdown_input
        del self.target_html_output
        del self.bootstrapRenderer
        del self.table_content_markdown_input
        del self.table_content_target_html_output
        del self.table_content_section

    def test_render(self) -> None:
        # test rendering simple content section ----------------------------
        # need to do some formatting to the rendered text
        bootstrap_section = self.bootstrapRenderer.render()
        bootstrap_section = self.test_utils.clean_text(bootstrap_section)

        # need to do some formatting to the test text
        target_output = self.target_html_output
        target_output = self.test_utils.clean_text(target_output)

        self.assertEqual(bootstrap_section, target_output)

    def test_render_content_section_with_table(self) -> None:
        # test rendering a content section that contains a table
        bootstrap_table_output = self.table_content_section.renderer.render()
        bootstrap_table_output = self.test_utils.clean_text(bootstrap_table_output)
        target_table_output = self.table_content_target_html_output
        target_table_output = self.test_utils.clean_text(target_table_output)

        self.assertEqual(bootstrap_table_output, target_table_output)

    def test_render_with_single_image_no_captions(self) -> None:
        # test rendering a single image that should have no figure around it.
        input = self.single_image_content_section.render()
        output = self.single_image_section_target_html_output
        input = self.test_utils.clean_text(input)
        output = self.test_utils.clean_text(output)
        self.assertEqual(input, output)

    def test_render_single_figure_with_caption(self) -> None:
        # test rendering a figure with an image and caption
        input = self.single_figure_content_section.render()
        output = self.single_figure_caption_html_output

        input = self.test_utils.clean_text(input)
        output = self.test_utils.clean_text(output)

        self.assertEqual(input, output)

    def test_render_single_figure_with_links(self) -> None:
        # test rendering a figure with an image, caption, and links
        input = self.single_figure_links_content_section.render()
        output = self.single_figure_links_html_output
        input = self.test_utils.clean_text(input)
        output = self.test_utils.clean_text(output)
        self.assertEqual(input, output)

    def test_render_three_figures_with_captions(self) -> None:
        input = self.three_figures_with_captions_content_sections.render()
        output = self.three_figures_with_captions_html_output
        input = self.test_utils.clean_text(input)
        output = self.test_utils.clean_text(output)
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
