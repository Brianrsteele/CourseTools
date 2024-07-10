from abc import ABC, abstractmethod


class ABCFigure(ABC):
    """
    This is an abstract class to define a figure. An image objects
    holds the file path and alt text information about an image file
    """

    # find the image information in the markdown content
    @abstractmethod
    def parse_image(self):
        pass

    # find the caption in the markdown content
    @abstractmethod
    def parse_caption(self):
        pass

    # find extra text like notes or links in the markdown content
    @abstractmethod
    def parse_text(self):
        pass

    # set a renderer object for the content section
    @abstractmethod
    def set_renderer(self, renderer):
        pass

    # render the section using the section's renderer object
    @abstractmethod
    def render():
        pass
