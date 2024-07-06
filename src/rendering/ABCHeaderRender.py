from abc import ABC, abstractmethod


class ABCHeaderRenderer(ABC):
    """
    Abstract class to a document header, or top portion,
    of a course document. Assumes the header is written in
    markdown. Tranlates the header into html or some other
    format.
    """

    @abstractmethod
    def render_header(self):
        pass
