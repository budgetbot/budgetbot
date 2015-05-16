import decimal

import unittest

import mock

from gspread import Worksheet

from ..backends import gspreadsheet


class TestGSpreadsheetBackend(unittest.TestCase):
    def setUp(self):
        self.backend = gspreadsheet.GSpreadsheetBackend()

    def test_balance1(self):
        """
        Positive amount.
        """
        worksheet = mock.Mock(spec=Worksheet)
        worksheet.acell.return_value.value = "Amount\n[ $88.88 ]"

        self.assertEqual(self.backend._balance(worksheet), decimal.Decimal("88.88"))

    def test_balance2(self):
        """
        Negative amount.
        """
        worksheet = mock.Mock(spec=Worksheet)
        worksheet.acell.return_value.value = "Amount\n[ -$88.88 ]"

        self.assertEqual(self.backend._balance(worksheet), decimal.Decimal("-88.88"))
