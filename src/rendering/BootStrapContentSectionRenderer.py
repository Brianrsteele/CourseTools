import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rendering.ABCRenderer import ABCRenderer
import markdown
import re
from documentModels.Image import Image
from rendering.BootStrapImageRenderer import BootStrapImageRenderer


class BootStrapSectionRenderer(ABCRenderer):
    def __init__(self, title, content):
        self.title = title.strip()
        self.content = content.strip()

    def render(self):
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
            if line.startswith("<li>"):
                line = "            " + line + "\n"
            else:
                line = "        " + line + "\n"
            return_text += line
        # get rid of the new line at the end of the section
        # return_text = return_text[:-1]
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
