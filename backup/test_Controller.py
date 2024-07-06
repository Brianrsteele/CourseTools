import unittest
import Controller


class Test_Controller(unittest.TestCase):

    def setUp(self) -> None:
        self.controller = Controller.Controller()
        self.content = """
            # Hello World #
        """

    def tearDown(self) -> None:
        del self.controller
        del self.content

    def test_parseMdTextToDocument(self) -> None:
        document = self.controller.parseMdTextToDocument(self.content)
        self.assertEqual(document.title, "Hello World")
                             
        


if __name__ == '__main__':
    unittest.main()