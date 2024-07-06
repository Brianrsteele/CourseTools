from abc import ABC, abstractmethod

class ABCSectionRenderer(ABC):
    """
        Abstract class to define an interface for rendering sections
        from markdown to another format, like HTML
    """

    @abstractmethod
    def render_section (self):
        pass