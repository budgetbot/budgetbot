import re
import gspread
import arrow

from oauth2client.client import SignedJwtAssertionCredentials

from .. import settings


class GSpreadsheetBackend(object):
    scope = ['https://spreadsheets.google.com/feeds']
    conn = None

    def _auth(self):
        credentials = SignedJwtAssertionCredentials(
            settings.GSPREAD_AUTH_EMAIL,
            settings.GSPREAD_AUTH_KEY,
            self.scope,
        )
        self.conn = gspread.authorize(credentials)
        return self.conn

    def _balance(self, worksheet):
        # This sucks
        regex = re.compile(r'\$(\d+\.\d+)')
        return float(regex.search(worksheet.acell("A2").value).groups()[0])

    def save(self, cat, amt, payee):
        if self.conn is None:
            self._auth()

        # Grab worksheet
        worksheet = self.conn.open(cat).sheet1

        # Read current balance from worksheet
        bal = self._balance(worksheet)

        # Append new row
        now = arrow.now(settings.TZ).datetime
        worksheet.append_row((amt, payee, "/".join(map(str, (now.month, now.day, now.year)))))

        # Return remaining balance
        return bal - amt
