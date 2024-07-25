import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rendering.ABCRenderer import ABCRenderer
from rendering.BootStrapImageRenderer import BootStrapImageRenderer
import markdown


class BootStrapFigureRenderer(ABCRenderer):
    def __init__(self, figure_object):
        self.figure = figure_object

    # <img class="img-fuid" src="./_images/depth-blur-1.jpg" alt="Water from a fountain spraying in the air in front of ice.">
    def render(self):
        return_html = ""
        return_html += '<figure class="w-50 m-4 shadow rounded figure">\n    '
        self.figure.image.set_renderer(BootStrapImageRenderer(self.figure.image))
        image_output = self.figure.image.render()
        image_output = image_output.replace(
            'class="img-fluid"', 'class="figure-img img-fluid"'
        )
        return_html += image_output + "\n    "
        return_html += '<figcaption class="m-4 figure-caption">\n'
        caption_output = markdown.markdown(self.figure.caption)
        return_html += caption_output + "\n    "
        return_html += "</figcaption>\n"
        if self.figure.text is not None:
            text = self.figure.text
            text = text.strip()
            html = markdown.markdown(text)
            html = html.replace("&amp;", "&")
            return_html += html + "\n"
        return_html += "</figure>"
        return return_html
