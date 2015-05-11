## Heroku config variables

```
heroku config:set GSPREAD_AUTH_EMAIL="$GSPREAD_AUTH_EMAIL"
heroku config:set GSPREAD_AUTH_KEY="`cat key`"
heroku config:set WEB_CONCURRENCY=3
heroku config:set TZ=CST
```