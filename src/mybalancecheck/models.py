from .backends.gspreadsheet import GSpreadsheetBackend


class Transaction(object):
    def __init__(self):
        self.backend = GSpreadsheetBackend()

    def save(self, cat, amt, payee):
        return self.backend.save(cat, amt, payee)
