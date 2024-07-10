import sys

sys.path.append(
    "/Users/briansteele/Library/CloudStorage/OneDrive-MNSCU/Development/CourseTools"
)

from documentModels.ABCFigure import ABCFigure
from documentModels.Image import Image


class Figure(ABCFigure):
    """
    Represents a figure with an Image object and its title, caption, and related text.
    """

    def __init__(self, content):
        self.markdown_content = content
        self.image = self.parse_image()
        self.caption = self.parse_caption()
        self.text = self.parse_text()
        self.renderer = None

    def __str__(self):
        return None

    def parse_image(self):
        """
        Find and create an image object.
        """
        image = None
        image_markdown = self.markdown_content.split("- ")[1]
        image = Image(image_markdown)
        return image

    def parse_caption(self):
        """
        Find the caption/title for the image.
        """
        caption = None
        caption = self.markdown_content.split("\n")[1]
        caption = caption.split("-")[1].strip()
        return caption

    def parse_text(self):
        """
        Find the text or links for the image.
        """
        text = None
        if self.markdown_content.split("-")[3:]:
            text = self.markdown_content.split("-")[3:]
            text = "-".join(text)
            text = "    -" + text
        return text

    def set_renderer(self, renderer):
        self.renderer = renderer

    def render(self):
        return self.renderer.render_image()
