#!/usr/bin/env python

from flask import Flask, render_template, request

from mybalancecheck import parser as _parser

app = Flask(__name__)
parser = _parser.Parser()


@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252, debug=True)
