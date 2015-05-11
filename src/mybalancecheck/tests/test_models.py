import unittest

from .. import models


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.tx = models.Transaction()

    def test_transaction1(self):
        self.assertIsNone(self.tx.save("Groceries", 24.17, "Publix"))
