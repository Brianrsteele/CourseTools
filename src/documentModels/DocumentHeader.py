import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from documentModels.ABCHeader import ABCHeader


class DocumentHeader(ABCHeader):
    """
    Represents the very first section markdown text in a document.
    Also potentially contains an author name and modified date
    for the document.
    """

    def __init__(self, content):
        self.raw_content = content
        self.title = self.parse_header_title()
        self.content = self.parse_header_content()
        self.author = self.parse_author()
        self.modified_date = self.parse_modified_date()
        self.renderer = None

    def __str__(self):
        return (
            f"Header: {self.title}, {self.author}, {self.modified_date}, {self.content}"
        )

    # find the header title in the raw content
    def parse_header_title(self):
        split_content = self.raw_content.split("\n")
        title = split_content[0]
        title = title[2:]
        return title

    # find the header content in the raw content
    def parse_header_content(self):
        content = ""
        content = self.raw_content.split("\n\n")
        if len(content) > 2:
            content = content[-1].strip()
        else:
            content = None
        return content

    # find the author in the raw content
    def parse_author(self):
        author = ""
        author = self.raw_content.split("\n")
        if len(author) > 2:
            for line in author:
                if line.startswith("Author"):
                    author = line
            author = author.split(":")
            author = author[1].strip()
        else:
            author = None
        return author

    # find the modified date in the raw content
    def parse_modified_date(self):
        modified_date = ""
        modified_date = self.raw_content.split("\n")
        if len(modified_date) > 2:
            for line in modified_date:
                if line.startswith("Modified Date"):
                    modified_date = line
            modified_date = modified_date.split(":")
            modified_date = modified_date[1].strip()
        else:
            modified_date = None
        return modified_date

    # set the renderer
    def set_renderer(self, renderer):
        self.renderer = renderer

    # render the content of the header using the assigned renderer
    def render(self):
        return self.renderer.render_header()
