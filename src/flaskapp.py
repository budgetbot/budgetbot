#!/usr/bin/env python
import logging

from flask import Flask, request

import twilio.twiml

from mybalancecheck import models
from mybalancecheck import parser as _parser
from mybalancecheck.parser.exceptions import ParserNoAmountException

import locale
locale.setlocale(locale.LC_ALL, "")

app = Flask(__name__)
parser = _parser.Parser()


@app.route("/", methods=['GET', 'POST'])
def index():
    return "Hello world!"


@app.route("/sms", methods=['GET', 'POST'])
def handler():
    message = request.values['Body']
    logging.info("Received '{}'.".format(message))

    resp = twilio.twiml.Response()

    try:
        try:
            # Parse message
            cat, amt, payee = parser.parse(message)

            # Save transaction
            tx = models.Transaction()
            remaining = tx.save(cat, amt, payee)

            # TODO
            # Use a template
            # Reply with confirmation and remaining amount
            reply = u"\U0001F44D {} at {} for {}. {} remaining.".\
                format(locale.currency(amt, grouping=True),
                       payee,
                       cat,
                       locale.currency(remaining, grouping=True))

        except ParserNoAmountException as e:
            # amt is 0, query for remaining budget in cat
            cat = e.args[0]

            budget = models.Budget(cat)
            remaining = budget.balance()

            reply = u"\U0001F44D {} remaining for {}.".\
                format(locale.currency(remaining, grouping=True),
                       cat)

    except Exception as e:
        # Log the exception
        logging.error("Error '{}'.".format(message))
        logging.exception(e)

        # Reply with misunderstood message
        reply = u"Sorry, no comprende \U0001F62D"

    resp.message(reply)
    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252, debug=True)
