import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rendering.ABCRenderer import ABCRenderer
import markdown


class BootStrapFooterRenderer(ABCRenderer):
    def __init__(self, footer):
        self.footer = footer
        if self.footer.content is not None:
            self.content = markdown.markdown(footer.content)
            self.content = self.content.strip()
        self.footer_content = ""

    def render(self):
        if self.footer.content is not None:
            self.footer_content += "        " + self.content + "\n"
        self.footer_content += "    </div>\n"
        self.footer_content += '    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"\n'
        self.footer_content += "        "
        self.footer_content += 'integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaA'
        self.footer_content += 'A55NDzOxhy9GkcIdslK1eN7N6jIeHz"'
        self.footer_content += ' crossorigin="anonymous">\n        </script>\n'
        self.footer_content += "</body>\n"
        self.footer_content += "\n"
        self.footer_content += "</html>"
        return self.footer_content
