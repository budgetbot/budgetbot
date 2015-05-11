import os

# Default timezone
TZ = os.environ.get("TZ", "CST")

# Used by mybalancecheck.backends.gspreadsheet.GSpreadsheetBackend to authenticate with Google Spreadsheets
# For steps to generate, see: https://gspread.readthedocs.org/en/latest/oauth2.html
GSPREAD_AUTH_EMAIL = os.environ.get("GSPREAD_AUTH_EMAIL")
GSPREAD_AUTH_KEY = os.environ.get("GSPREAD_AUTH_KEY")
