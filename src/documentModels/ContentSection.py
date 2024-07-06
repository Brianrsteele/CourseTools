import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from documentModels.ABCSection import ABCSection


class ContentSection(ABCSection):
    """
    Represents a section of markdown text from an assignment that has a title, intro
    paragraph and then a bullet pointed list of instructions
    """

    def __init__(self, content):
        self.raw_content = content
        self.title = self.parse_section_title()
        self.content = self.parse_section_content()
        self.renderer = None

    def __str__(self):
        return f"ContentSection: {self.title}, {self.content}"

    def parse_section_title(self):
        """
        Find the title of the section in the raw markdown
        """
        title = self.raw_content.split("\n")[0]
        title = title.replace("##", "")
        title = title.strip()
        return title

    def parse_section_content(self):
        """
        Find the content of the section in the raw markdown
        """
        content = self.raw_content.split("\n")[2:]
        content = "\n".join(content)
        content = content.strip()
        return content

    def remove_bold(self):
        """
        Remove "**" sequences which would represent <strong> text in markdown
        """
        nobold = self.content.replace("**", "")
        return nobold

    def set_renderer(self, renderer):
        self.renderer = renderer

    def render(self):
        return self.renderer.render_section()
