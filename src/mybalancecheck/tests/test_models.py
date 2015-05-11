import unittest

import mock

from .. import models


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.gspreadsheet_patcher = mock.patch("mybalancecheck.models.GSpreadsheetBackend")
        self.gspreadsheet = self.gspreadsheet_patcher.start()

    def test_transaction1(self):
        self.tx = models.Transaction()
        self.gspreadsheet.return_value.save.return_value = 44.44
        self.assertEqual(self.tx.save("Groceries", 88.88, "Publix"), 44.44)
        self.assertListEqual(self.gspreadsheet.mock_calls, [
            mock.call(),
            mock.call().save("Groceries", 88.88, "Publix")
        ])

    def tearDown(self):
        self.gspreadsheet_patcher.stop()
