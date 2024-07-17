import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rendering.ABCRenderer import ABCRenderer
from rendering.BootStrapHeaderRenderer import BootStrapHeaderRenderer
from rendering.BootStrapFooterRenderer import BootStrapFooterRenderer
from rendering.BootStrapContentSectionRenderer import BootStrapSectionRenderer
import markdown


class BootStrapDocumentRenderer(ABCRenderer):
    def __init__(self, document):
        self.document = document

    def render(self, document):
        rendered_document_string = ""
        document.header.set_renderer(BootStrapHeaderRenderer(self.document.header))
        document.footer.set_renderer(BootStrapFooterRenderer(self.document.footer))
        rendered_document_string += self.document.header.render()
        rendered_document_string += "\n"
        for section in self.document.sections:
            section.set_renderer(BootStrapSectionRenderer(section))
            rendered_document_string += section.render()
        rendered_document_string += "\n"
        rendered_document_string += self.document.footer.render()

        return rendered_document_string
