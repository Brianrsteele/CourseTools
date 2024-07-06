from abc import ABC, abstractmethod


class ABCFooter(ABC):
    """
    This is an abstract class to define a footer. A footer is the final section of
      a document. Assumes the footer is written in markdown.
    """

    # find the footer content in the raw content
    @abstractmethod
    def parse_footer_content(self):
        pass

    # set the renderer
    @abstractmethod
    def set_renderer(self, renderer):
        pass

    @abstractmethod
    def render(self):
        pass
