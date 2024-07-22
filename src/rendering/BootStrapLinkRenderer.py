import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rendering.ABCRenderer import ABCRenderer


class BootStrapLinkRenderer(ABCRenderer):
    def __init__(self, link_object):
        self.link = link_object

    def render(self):
        return_html = ""
        return_html += '<a href="'
        return_html += self.link.url
        return_html += '" class="link-primary link-offset-2" target="_blank">'
        return_html += self.link.link_text
        return_html += "</a>"
        return return_html
