import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rendering.ABCRenderer import ABCRenderer


class BootStrapImageRenderer(ABCRenderer):
    def __init__(self, image_object):
        self.image = image_object

    # <img class="img-fuid" src="./_images/depth-blur-1.jpg" alt="Water from a fountain spraying in the air in front of ice.">
    def render(self):
        return_html = ""
        return_html += '<img class="img-fuid" src="'
        return_html += self.image.path
        return_html += '" alt="'
        return_html += self.image.alt_text
        return_html += '">'
        return return_html
