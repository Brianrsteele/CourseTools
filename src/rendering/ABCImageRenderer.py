from abc import ABC, abstractmethod


class ABCImageRenderer(ABC):
    """
    Abstract class to render the an image object. Assumes the footer is written in markdown and
    translates the image to html or some other format.
    """

    @abstractmethod
    def render_image(self):
        pass
