from .backends.gspreadsheet import GSpreadsheetBackend


class Budget(object):
    def __init__(self, cat):
        self.backend = GSpreadsheetBackend()
        self.cat = cat

    def balance(self):
        return self.backend.balance(self.cat)


class Transaction(object):
    def __init__(self):
        self.backend = GSpreadsheetBackend()

    def save(self, cat, amt, payee):
        return self.backend.save(cat, amt, payee)
