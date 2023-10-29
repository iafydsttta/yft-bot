# YFT Bot

YFT stands for Yahoo Finance + Telegram.

It's a Telegram bot that uses the [yfinance](https://github.com/ranaroussi/yfinance) library. **NOTE:** yfinance is currently not working, see this github [issue](https://github.com/ranaroussi/yfinance/issues/1729).

[Code](./src/bot.py) takes inspiration from this [tutorial](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot).

## Preparation

- Get an API token from "BotFather", see Telegram docs.
- Set as environment variable: export `TELEGRAMTOKEN=<token>` or add to .env file.

## Start a responsive bot

```python
python src/reponsive.py
```

## Start a bot that sends scheduled messages

```python
python src/periodic.py
```
