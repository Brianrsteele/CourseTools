
from Document import Document


class Controller():

    def parseMdTextToDocument(self,md_text):
        start = md_text.find("#")
        end = md_text.find("#\n")
        title = md_text[(start + 1): end]
        title = title.strip()
        document = Document(title)
        return document