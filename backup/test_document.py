import datetime
import ABCSection
import Document
import unittest

class Test_Document(unittest.TestCase):
    section_1: ABCSection.Section = ABCSection.Section("Title 1", "Content 1")
    section_2: ABCSection.Section = ABCSection.Section("Title 2", "Content 2")
    section_3: ABCSection.Section = ABCSection.Section("Title 3", "Content 3")
    my_document: Document.Document = Document.Document("test document")
    now: datetime.datetime = datetime.datetime.now()

    def test_init(self) -> None:
        self.assertEqual(self.my_document.title, "test document")
        self.assertEqual(self.my_document.documentContent, [])







                             
        


if __name__ == '__main__':
    unittest.main()