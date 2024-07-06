from abc import ABC, abstractmethod


class ABCDocument(ABC):
    """
    Abstract class to define a document to hold course instructions,
    FAQ's, and other information
    """

    # parse the contents of the document
    @abstractmethod
    def parse_document(self):
        pass

    # create a header for the document
    @abstractmethod
    def add_header(self):
        pass

    # create a footer for the document
    @abstractmethod
    def add_footer(self):
        pass

    # add a section to the document in order
    @abstractmethod
    def append_section(self, section):
        pass

    # render the document
    @abstractmethod
    def render_document(self, type):
        pass
