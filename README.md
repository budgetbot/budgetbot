# Budgetbot

Frictionless, mobile budgeting, driven by SMS, powered by Google Spreadsheets.

Check it out...

![](https://budgetbot.s3.amazonaws.com/budgetbot.3.gif)

## Setup

    git clone git@github.com:budgetbot/budgetbot.git
    pip install -r requirements.txt
    heroku apps:create mybudgetbotclone
    heroku config:set GSPREAD_AUTH_EMAIL="`cat email`"  # https://gspread.readthedocs.org/en/latest/oauth2.html
    heroku config:set GSPREAD_AUTH_KEY="`cat key`"  # https://gspread.readthedocs.org/en/latest/oauth2.html
    heroku config:set WEB_CONCURRENCY=3
    heroku config:set TZ=CST


### To do

- [ ] Better README!
- [ ] More emoji!
- [ ] Get a budget status report with `?`.
- [ ] Amend budget.
- [ ] Multiple users / budgets.
- [ ] Multiple back-ends (other than Google Spreadsheets).
- [ ] AI, e.g. auto-identify category from payee, warnings when close to overspending in category.
- [ ] Connect with [Plaid](https://plaid.com/), consolidate with bank account, identify missing transactions.
- [ ] :moneybag:

## Contact

Get in touch with me on the [Twitters](https://twitter.com/steveWINton).
