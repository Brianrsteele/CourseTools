import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from documentModels.ABCDocumentModel import ABCDocumentModel
from documentModels.DocumentHeader import DocumentHeader
from documentModels.DocumentFooter import DocumentFooter
from documentModels.ContentSection import ContentSection
from rendering.BootStrapHeaderRenderer import BootStrapHeaderRenderer
from rendering.BootStrapFooterRenderer import BootStrapFooterRenderer
from rendering.BootStrapContentSectionRenderer import BootStrapSectionRenderer


class Document(ABCDocumentModel):
    """
    Represents writing for a class assignment, FAQ, syllabus, or other material
    that is written in markdown and then converted to other formats, like HTML
    or DOCX.


    """

    def __init__(self, content):
        self.raw_content = content
        self.header = None
        self.footer = None
        self.sections = []
        self.parse()

    def __str__(self):
        return_string = ""
        return_string += "Document:\n"
        return_string += f"{self.header}\n"
        for section in self.sections:
            return_string += f"{section}\n"
        return_string += f"{self.footer}"
        return return_string

    def parse(self):
        self.add_header()
        self.add_footer()
        my_sections = self.parse_all_sections_text()
        for section in my_sections:
            self.append_section(section)

    def add_header(self):
        # When this method is complete, the document object should have a
        # header object that was parsed from the markdown
        self.header = DocumentHeader(self.parse_header())

    def parse_header(self):
        # uses the self.raw_content markdown text to find and return
        # the markdown content to create a header.
        header_markdown = ""
        header_markdown = self.raw_content.split("##")[0]
        header_markdown = header_markdown.strip()
        return header_markdown

    def add_footer(self):
        # When this method is complete, the document object should have a
        # footer object that was parsed from the markdown
        self.footer = DocumentFooter(self.parse_footer())

    def parse_footer(self):
        # uses the self.raw_content markdown text to find and return
        # the markdown content to create a footer.
        footer_markdown = ""
        footer_markdown = self.raw_content.split("## Footer")[1].strip()
        return footer_markdown

    def append_section(self, section_text):
        # When this method is complete, a section object should be
        # appended to the self.sections list
        new_section = ContentSection(section_text)
        self.sections.append(new_section)
        return self.sections

    def parse_all_sections_text(self):
        # uses the self.raw_content markdown text to find and return
        # the markdown content to create the sections in the form of a list with
        # the string form of each section, starting with the title.
        # Should not include a header or footer section.
        all_sections = self.raw_content.split("\n\n## ")
        all_sections = all_sections[1:-1]
        return all_sections

    def set_renderer(self, renderer):
        pass

    def render(self, type):
        # when this method is completed, it should return a string with the
        # html, docx, or other information needed to save as a file of the
        # requested type.
        rendered_document_string = ""
        type = type.upper()
        if type == "BOOTSTRAP":
            self.header.set_renderer(BootStrapHeaderRenderer(self.header))
            self.footer.set_renderer(BootStrapFooterRenderer(self.footer))
            rendered_document_string += self.header.render()
            rendered_document_string += "\n"
            for section in self.sections:
                section.set_renderer(
                    BootStrapSectionRenderer(section.title, section.content)
                )
                rendered_document_string += section.render()
            rendered_document_string += "\n"
            rendered_document_string += self.footer.render()

        return rendered_document_string
