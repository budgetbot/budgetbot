#!/usr/bin/env python

"""
From: https://gspread.readthedocs.org/en/latest/oauth2.html
"""

import json
import re
import gspread
import arrow

from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('My Balance Check-74d33539077f.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

wks = gc.open("Groceries").sheet1

# Current balance
data = wks.acell("A2").value
regex = re.compile(r'\$(\d+\.\d+)')
print float(regex.search(data).groups()[0])

# Add tx
now = arrow.now("CST").datetime
wks.append_row((15.0, "Publix", "/".join(map(str, (now.month, now.day, now.year)))))
