import sys

sys.path.append(
    "/Users/briansteele/Library/CloudStorage/OneDrive-MNSCU/Development/CourseTools"
)

from documentModels.ABCDocumentModel import ABCDocumentModel


class Link(ABCDocumentModel):
    """
    Represents a hyperlink with associated text and attributes
    """

    def __init__(self, content):
        self.markdown_content = content
        self.parse()
        self.renderer = None

    def __str__(self):
        return f"{self.image}: {self.caption}\n{self.text}"

    def parse(self):
        self.url = self.parse_url()
        self.link_text = self.parse_link_text()

    def parse_url(self):
        """
        Find the URL for the link
        """
        url = self.markdown_content
        url = url.split("](")[1].strip()
        url = url[:-1]
        return url

    def parse_link_text(self):
        """
        Find the text of the link
        """
        link_text = self.markdown_content
        link_text = link_text.split("](")[0].strip()
        link_text = link_text[2:]
        return link_text

    def set_renderer(self, renderer):
        self.renderer = renderer

    def render(self):
        return self.renderer.render()
