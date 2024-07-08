import sys

sys.path.append(
    "/Users/briansteele/Library/CloudStorage/OneDrive-MNSCU/Development/CourseTools"
)

from documentModels.ABCImage import ABCImage


class Image(ABCImage):
    """
    Represents an image with a file path to an image file and
    alt text describing the image.
    """

    def __init__(self, content):
        self.markdown_content = content
        self.path = self.parse_image_path()
        self.alt_text = self.parse_alt_text()
        self.renderer = None

    def __str__(self):
        return f"Image: {self.path}, {self.alt_text}"

    def parse_image_path(self):
        """
        Find the path to the image file in the raw markdown
        """
        path = ""
        path = self.markdown_content.split("](")[1]
        path = path.strip()
        path = path[:-1]
        return path

    # ![Water from a fountain spraying in the air in front of ice.](./_images/depth-blur-1.jpg)

    def parse_alt_text(self):
        """
        Find the alt tag text for the image in the raw markdown
        """
        alt_text = ""
        alt_text = self.markdown_content.split("](")[0][2:]
        return alt_text

    def set_renderer(self, renderer):
        self.renderer = renderer

    def render(self):
        return self.renderer.render_image()
