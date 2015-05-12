# Budgetbot

Frictionless, mobile budgeting, driven by SMS, powered by Google Spreadsheets.

Check it out...

![](https://budgetbot.s3.amazonaws.com/budgetbot.3.gif)

## Setup

1. `git clone git@github.com:budgetbot/budgetbot.git`
2. `pip install -r requirements.txt`
3. `heroku apps:create mybudgetbotclone`
4. `heroku config:set GSPREAD_AUTH_EMAIL="$GSPREAD_AUTH_EMAIL"`
5. `heroku config:set GSPREAD_AUTH_KEY="`cat key`"`
6. `heroku config:set WEB_CONCURRENCY=3`
7. `heroku config:set TZ=CST`


### To do

- [ ] Query remaining budget for month via `Groceries?`, `Fuel?`, `Restaurants?`.


## Contact

[steveWINton](https://twitter.com/steveWINton).
