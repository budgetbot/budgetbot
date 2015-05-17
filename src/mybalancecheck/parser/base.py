import decimal
import re
import string

from ..categories import categories

from .exceptions import ParserNoAmountException


class Parser():
    amt_regex = re.compile(r"[-+]?\$?\d*\.\d+|\d+")

    def category(self, message):
        for category, representations in categories.items():
            for representation in representations:
                if message.lstrip().startswith(representation):
                    return category, representation
        # Nothing found, return first entity within message
        unknown = message.split()[0]
        return unknown.title(), unknown

    def amount(self, message):
        amt = self.amt_regex.findall(message)[0]
        return decimal.Decimal(amt.replace('$', '')), amt

    def parse(self, message):
        # Extracts "Category", "Amount", "Payee" from message and returns as
        # a tuple
        cat, cat_representation = self.category(message)

        try:
            amt, amt_representation = self.amount(message)

        except Exception:
            raise ParserNoAmountException(cat, message)

        # Strip representation and amt from message
        message = message.replace(cat_representation, "").replace(amt_representation, "")
        payee = string.capwords(message.lstrip().rstrip()) or ""

        return (cat, amt, payee)