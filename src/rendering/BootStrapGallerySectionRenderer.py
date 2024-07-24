import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from documentModels.Figure import Figure
from rendering.BootStrapSectionRenderer import BootStrapSectionRenderer
from rendering.BootStrapGalleryFigureRenderer import BootStrapGalleryFigureRenderer
import markdown


class BootStrapGallerySectionRenderer(BootStrapSectionRenderer):
    def __init__(self, content_section):
        super().__init__(content_section)

    def render(self):
        return_bootstrap = ""
        self.content = super().parse_links()
        self.content = self.parse_gallery_figures()
        id = self.title
        id = id.replace(" ", "_")
        id = id.lower()
        return_bootstrap += '<h2 id="' + id + '">' + self.title + "</h2>\n"
        return_bootstrap += '<div class="container">\n'
        return_bootstrap += markdown.markdown(self.content, extensions=["tables"])
        return_bootstrap = super().format_indents(return_bootstrap)
        return_bootstrap += "</div>\n"
        return return_bootstrap

    def parse_gallery_figures(self):
        content = self.content
        if "- ![" not in self.content:
            return self.content
        else:
            raw_figure_list = content.split("- ![]")
            for raw_figure in raw_figure_list:
                raw_figure = raw_figure.split("\n\n")
                raw_figure = "".join(raw_figure[0])
                individual_figures = raw_figure.split("- ![")
                # a list of images with captions will be parsed as
                # a figure with a bunch of text. We need to
                # further parse subsequent images into their own
                # figures. If there is only one individual figure
                # then the loop only goes around once.
                #
                # start at [1:] to get rid of empty string
                # at front of the list returned from split

            self.content = self.process_figure_list(self.content, individual_figures)
        return self.content

    def process_figure_list(self, content, individual_figures):
        figure_count = len(individual_figures[1:])
        number_of_columns = 3
        count = 0
        for figure in individual_figures[1:]:
            figure = "- ![" + figure
            new_figure = Figure(figure)
            new_figure_text = ""

            if count % number_of_columns == 0:
                new_figure_text += '<div class="row">\n'
            new_figure.set_renderer(BootStrapGalleryFigureRenderer(new_figure))
            new_figure_text += new_figure.render()
            if count % number_of_columns == 2:
                new_figure_text += "</div>\n"

            if (figure_count == count + 1) and (figure_count % number_of_columns != 0):
                new_figure_text += "</div>\n"

            content = content.replace(figure, new_figure_text, 1)

            count = count + 1
            # print(count)
        return content
