import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rendering.ABCRenderer import ABCRenderer
import markdown
import re
from documentModels.Image import Image
from documentModels.Figure import Figure
from rendering.BootStrapImageRenderer import BootStrapImageRenderer
from rendering.BootStrapFigureRenderer import BootStrapFigureRenderer


class BootStrapSectionRenderer(ABCRenderer):
    def __init__(self, content_section):
        self.title = content_section.title.strip()
        self.content = content_section.content.strip()

    def render(self):
        self.content = self.parse_figures()
        self.parse_single_images_without_captions()
        return_bootstrap = ""
        id = self.title
        id = id.replace(" ", "_")
        id = id.lower()
        return_bootstrap += '<h2 id="' + id + '">' + self.title + "</h2>\n"
        return_bootstrap += markdown.markdown(self.content, extensions=["tables"])
        return_bootstrap = self.format_indents(return_bootstrap)

        if "table" in return_bootstrap:
            return_bootstrap = self.make_tables_pretty(return_bootstrap)

        return return_bootstrap

    # In order to match VScode Prettier formatting,
    # indents of four spaces need to be added to each line
    # and eight spaces for each <li>
    def format_indents(self, text):
        return_text = ""
        text_lines = text.split("\n")
        for line in text_lines:
            if len(line) == 0:
                pass
            else:
                if line.startswith("<li>"):
                    line = "            " + line + "\n"
                else:
                    line = "        " + line + "\n"
                return_text += line
        return return_text

    def make_tables_pretty(self, text):
        text = re.sub("(<table)", '<table class="table table-striped"', text)
        return text

    def parse_single_images_without_captions(self):
        images = re.findall("!\[.*\]\(.*\)", self.content)
        for image in images:
            replacement_image = Image(image)
            replacement_image.set_renderer(BootStrapImageRenderer(replacement_image))
            replacement_image_tag = replacement_image.render()
            self.content = self.content.replace(image, replacement_image_tag)

    def parse_figures(self):
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
                for figure in individual_figures[1:]:
                    figure = "- ![" + figure
                    new_figure = Figure(figure)
                    new_figure.set_renderer(BootStrapFigureRenderer(new_figure))
                    content = content.replace(figure, new_figure.render())
            self.content = content
        return self.content
