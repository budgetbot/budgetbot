#!/usr/bin/env python
import logging

from flask import Flask, request

import twilio.twiml

from mybalancecheck import models
from mybalancecheck import parser as _parser

app = Flask(__name__)
parser = _parser.Parser()


@app.route("/", methods=['GET', 'POST'])
def index():
    return "Hello world!"


@app.route("/sms", methods=['GET', 'POST'])
def handler():
    message = request.values['Body']
    resp = twilio.twiml.Response()

    try:
        # Parse message
        cat, amt, payee = parser.parse(message)

        # Save transaction
        tx = models.Transaction()
        remaining = tx.save(cat, amt, payee)

        # Reply with confirmation and remaining amount
        reply = "Got it! Remaining: ${:,.2f}.".format(remaining)

    except Exception as e:
        # Log the exception
        logging.exception(e)

        # Reply with misunderstood message
        reply = "Sorry, no comprende :("

    resp.message(reply)
    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252, debug=True)
