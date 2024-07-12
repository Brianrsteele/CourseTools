from abc import ABC, abstractmethod


class ABCDocumentModel(ABC):
    """
    Abstract class to define the methods document and the parts of a document.
    """

    # parse the contents of the document
    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def set_renderer(self, renderer):
        pass

    # render the document
    @abstractmethod
    def render(self, type):
        pass
