# YFT Bot

YFT stands for Yahoo Finance + Telegram.

It's a Telegram bot that uses the [yfinance](https://github.com/ranaroussi/yfinance) library.

[Code](./src/yft_bot/bot.py) takes inspiration from this [tutorial](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot).

## Preparation

- Get an API token from "BotFather", see Telegram docs.
- Set as environment variable: export `TELEGRAMTOKEN=<token>` or add to .env file.

## Start the bot

```python
python src/yft_bot/main.py
```

## Send a debug message

```python
python src/yft_bot/debug.py
```
