import re


from .categories import categories


class Parser():
    amt_regex = re.compile(r"[-+]?\d*\.\d+|\d+")

    def category(self, message):
        for category, representations in categories.items():
            for representation in representations:
                if message.lstrip().startswith(representation):
                    return category, representation

    def amount(self, message):
        amt = self.amt_regex.findall(message)[0]
        return float(amt), amt

    def parse(self, message):
        # Extracts "Category", "Amount", "Payee" from message and returns as
        # a tuple
        cat, cat_representation = self.category(message)
        amt, amt_representation = self.amount(message)

        # Strip representation and amt from message
        message = message.replace(cat_representation, "").replace(amt_representation, "")
        payee = message.lstrip().rstrip()
        return (cat, amt, payee)
