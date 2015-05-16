import decimal
import unittest

from .. import parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()
        self.amt = decimal.Decimal("88.88")

    def test_parser1(self):
        """
        Basic entity recognition.
        """
        message = "Groceries 88.88 Publix"
        self.assertEqual(("Groceries", self.amt, "Publix"), self.parser.parse(message))

    def test_parser2(self):
        """
        Lower-case category.
        """
        message = "groceries 88.88 Publix"
        self.assertEqual(("Groceries", self.amt, "Publix"), self.parser.parse(message))

    def test_parser3(self):
        """
        Category abbreviation.
        """
        message = "groc 88.88 Publix"
        self.assertEqual(("Groceries", self.amt, "Publix"), self.parser.parse(message))

    def test_parser4(self):
        """
        Different category abbreviation.
        """
        message = "groc. 88.88 Publix"
        self.assertEqual(("Groceries", self.amt, "Publix"), self.parser.parse(message))

    def test_parser5(self):
        """
        Multi-word payee and whitespace.
        """
        message = "groc. 88.88    Harris Teeter   "
        self.assertEqual(("Groceries", self.amt, "Harris Teeter"), self.parser.parse(message))

    def test_parser6(self):
        """
        Negative amount left intact.
        """
        message = "groc. -88.88    Harris Teeter   "
        self.assertEqual(("Groceries", -self.amt, "Harris Teeter"), self.parser.parse(message))

    def test_parser7(self):
        """
        Amount returned as float.
        """
        message = "Groc. 88.88    Harris Teeter   "
        self.assertEqual(("Groceries", self.amt, "Harris Teeter"), self.parser.parse(message))

    def test_parser8(self):
        """
        Whitespace at end of message, different ordering of entities in message.
        """
        message = "Groc.     Harris Teeter   88.88\n"
        self.assertEqual(("Groceries", self.amt, "Harris Teeter"), self.parser.parse(message))

    def test_parser9(self):
        """
        Whitespace at start and end of message.
        """
        message = "\nGroc.     Harris Teeter   88.88\n"
        self.assertEqual(("Groceries", self.amt, "Harris Teeter"), self.parser.parse(message))

    def test_parser10(self):
        """
        No payee.
        """
        message = "Groc.   88.88\n"
        self.assertEqual(("Groceries", self.amt, ""), self.parser.parse(message))

    def test_parser11(self):
        """
        Capitalization of payee.
        """
        message = "groc.   harris teeter 88.88\n"
        self.assertEqual(("Groceries", self.amt, "Harris Teeter"), self.parser.parse(message))

    def test_parser12(self):
        """
        Dollar symbol used with amount.
        """
        message = "groc. $88.88 Publix"
        self.assertEqual(("Groceries", self.amt, "Publix"), self.parser.parse(message))

    def test_parser13(self):
        """
        Unknown category should be returned verbatim.
        """
        message = "other 88.88 Academy"
        self.assertEqual(("Other", self.amt, "Academy"), self.parser.parse(message))

    def test_parser14(self):
        """
        No amount.
        """
        message = "Groceries"
        self.assertEqual(("Groceries", 0.0, ""), self.parser.parse(message))

    def test_parser15(self):
        """
        Apostrophe in payee.
        """
        message = "restaurants 88.88 zaxby's"
        self.assertEqual(("Restaurants", self.amt, "Zaxby's"), self.parser.parse(message))

    def test_parser16(self):
        """
        Dollar symbol used with negative amount.
        """
        message = "groc. -$88.88 Publix"
        self.assertEqual(("Groceries", -self.amt, "Publix"), self.parser.parse(message))
