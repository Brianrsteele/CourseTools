import ABCSection



class Document():
    def __init__(self, title: str) -> None:
        self.title: str = title
        self.documentContent: list[ABCSection.Section] = []


    def addSection(self, section) -> None:
        # add a section object to the documentContent and add a section order number
        self.documentContent.append(section)
