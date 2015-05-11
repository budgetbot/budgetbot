#!/usr/bin/env python

from flask import Flask, render_template, request

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
    resp = twilio.twiml.Response()
    resp.message("Hello world!")
    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252, debug=True)
