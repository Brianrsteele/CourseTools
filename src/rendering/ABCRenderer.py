from abc import ABC, abstractmethod


class ABCRenderer(ABC):
    """
    Abstract class to render the output of a document or part of a document.
    """

    @abstractmethod
    def render(self):
        pass
