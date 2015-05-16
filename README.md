# Budgetbot

Frictionless, mobile budgeting, driven by SMS, powered by Google Spreadsheets.

Check it out...

![](https://budgetbot.s3.amazonaws.com/budgetbot.3.gif)

## Setup

    git clone git@github.com:budgetbot/budgetbot.git
    pip install -r requirements.txt
    heroku apps:create mybudgetbotclone
    heroku config:set GSPREAD_AUTH_EMAIL="$GSPREAD_AUTH_EMAIL"
    heroku config:set GSPREAD_AUTH_KEY="`cat key`"
    heroku config:set WEB_CONCURRENCY=3
    heroku config:set TZ=CST


### To do

- [ ] Query remaining budget for month via `Groceries?`, `Fuel?`, `Restaurants?`.


## Contact

[steveWINton](https://twitter.com/steveWINton).
