from abc import ABC, abstractmethod


class ABCHeader(ABC):
    """
    This is an abstract class to define a Header. A header is the
    first portion of a document that contains the document's title.
    Assumes the header is written in markdown.
    """

    # find the header title in the raw content
    @abstractmethod
    def parse_header_title(self):
        pass

    # find the header content in the raw content
    @abstractmethod
    def parse_header_content(self):
        pass

    # find the author in the raw content
    @abstractmethod
    def parse_author(self):
        pass

    # find the author in the raw content
    @abstractmethod
    def parse_modified_date(self):
        pass

    # set the renderer
    @abstractmethod
    def set_renderer(self, header):
        pass

    # render the header
    @abstractmethod
    def render(self):
        pass
