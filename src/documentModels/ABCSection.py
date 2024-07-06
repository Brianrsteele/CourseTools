from abc import ABC, abstractmethod


class ABCSection(ABC):
    """
    This is an abstract class to define a section. A section is a portion
    of a document with a title and some content.
    """

    # find the section title in the raw content
    @abstractmethod
    def parse_section_title(self):
        pass

    # find the section title in the raw content
    @abstractmethod
    def parse_section_content(self):
        pass

    # set a renderer object for the content section
    @abstractmethod
    def set_renderer(self, renderer):
        pass

    # render the section using the section's renderer object
    @abstractmethod
    def render():
        pass
