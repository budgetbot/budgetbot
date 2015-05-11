import unittest

from .. import parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_parser1(self):
        message = "Groceries 24.17 Publix"
        self.assertEqual(("Groceries", 24.17, "Publix"), self.parser.parse(message))

    def test_parser2(self):
        message = "groceries 24.17 Publix"
        self.assertEqual(("Groceries", 24.17, "Publix"), self.parser.parse(message))

    def test_parser3(self):
        message = "groc 24.17 Publix"
        self.assertEqual(("Groceries", 24.17, "Publix"), self.parser.parse(message))

    def test_parser4(self):
        message = "groc. 24.17 Publix"
        self.assertEqual(("Groceries", 24.17, "Publix"), self.parser.parse(message))

    def test_parser5(self):
        message = "groc. 24.17    Harris Teeter   "
        self.assertEqual(("Groceries", 24.17, "Harris Teeter"), self.parser.parse(message))

    def test_parser6(self):
        message = "groc. -24.17    Harris Teeter   "
        self.assertEqual(("Groceries", -24.17, "Harris Teeter"), self.parser.parse(message))

    def test_parser7(self):
        message = "Groc. 24    Harris Teeter   "
        self.assertEqual(("Groceries", 24.0, "Harris Teeter"), self.parser.parse(message))

    def test_parser8(self):
        message = "Groc.     Harris Teeter   24\n"
        self.assertEqual(("Groceries", 24.0, "Harris Teeter"), self.parser.parse(message))

    def test_parser9(self):
        message = "\nGroc.     Harris Teeter   24\n"
        self.assertEqual(("Groceries", 24.0, "Harris Teeter"), self.parser.parse(message))

    def test_parser10(self):
        message = "Groc.   24\n"
        self.assertEqual(("Groceries", 24.0, ""), self.parser.parse(message))

    def test_parser11(self):
        message = "groc.   harris teeter 24\n"
        self.assertEqual(("Groceries", 24.0, "Harris Teeter"), self.parser.parse(message))
