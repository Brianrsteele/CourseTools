import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from documentModels.ABCDocumentModel import ABCDocumentModel


class DocumentFooter(ABCDocumentModel):
    """
    Represents the very last section markdown text in a document.
    Also potentially contains some content for the end of the document.
    """

    def __init__(self, content):
        self.raw_content = content
        self.parse()
        self.renderer = None

    def __str__(self):
        return f"Footer: {self.content}"

    def parse(self):
        self.content = self.parse_footer_content()

    # find the footer content in the raw content
    def parse_footer_content(self):
        content = self.raw_content
        if len(content) > 0:
            content = self.raw_content.strip()
        else:
            content = None
        return content

    # set the renderer
    def set_renderer(self, renderer):
        self.renderer = renderer

    # render the footer contents
    def render(self):
        return self.renderer.render()
