from abc import ABC, abstractmethod


class ABCFooterRenderer(ABC):
    """
    Abstract class to render the output of a footer, or bottom portion
    of a course document. Assumes the footer is written in markdown and
    translates the footer to html or some other format.
    """

    @abstractmethod
    def render_footer(self):
        pass
