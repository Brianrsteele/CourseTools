from abc import ABC, abstractmethod


class ABCImage(ABC):
    """
    This is an abstract class to define an image. An image objects
    holds the file path and alt text information about an image file
    """

    # find the image path in the markdown content
    @abstractmethod
    def parse_image_path(self):
        pass

    # find the alt text in the markdown content
    @abstractmethod
    def parse_alt_text(self):
        pass

    # set a renderer object for the content section
    @abstractmethod
    def set_renderer(self, renderer):
        pass

    # render the section using the section's renderer object
    @abstractmethod
    def render():
        pass
