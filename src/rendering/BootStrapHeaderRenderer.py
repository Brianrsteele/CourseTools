import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rendering.ABCRenderer import ABCRenderer
import markdown


class BootStrapHeaderRenderer(ABCRenderer):
    def __init__(self, header):
        self.header = header
        self.header_render_content = ""
        self.title = header.title
        self.content = header.content
        self.modified_date = header.modified_date
        self.author = header.author

    def render(self):
        header_render_content = ""
        header_render_content += "<!doctype html>\n"
        header_render_content += '<html lang="en">'
        header_render_content += "\n\n"
        header_render_content += "<head>\n"
        header_render_content += '    <meta charset="utf-8">\n'
        header_render_content += (
            '    <meta name="viewport" content="width=device-width, '
        )
        header_render_content += 'initial-scale=1">\n'
        if self.title:
            header_render_content += "    <title>" + self.title + "</title>\n"
        header_render_content += '    <link href="'
        header_render_content += "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/"
        header_render_content += 'css/bootstrap.min.css" rel="stylesheet"\n'
        header_render_content += '        integrity="'
        header_render_content += (
            "sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0"
        )
        header_render_content += 'JMhjY6hW+ALEwIH" crossorigin="anonymous">\n'
        header_render_content += "</head>"
        header_render_content += "\n\n"
        header_render_content += "<body>\n"
        header_render_content += '    <div class="container-md">\n'
        if self.title:
            header_render_content += "        <h1>" + self.title + "</h1>\n"
        if self.author and self.modified_date:
            header_render_content += (
                '        <small class="text-body-secondary">'
                + self.author
                + ", "
                + self.modified_date
                + "</small>\n"
            )
        elif self.author:
            header_render_content += (
                '        <small class="text-body-secondary">'
                + self.author
                + "</small>\n"
            )
        elif self.modified_date:
            header_render_content += (
                '        <small class="text-body-secondary">'
                + self.modified
                + "</small>\n"
            )
        if self.content:
            header_render_content += "        " + markdown.markdown(self.content)
        return header_render_content
