# YFT Bot

## TOC

- [YFT Bot](#yft-bot)
  - [TOC](#toc)
  - [Preparation](#preparation)
  - [Start a responsive bot](#start-a-responsive-bot)
  - [Start a bot that sends a message if more than X time has passed](#start-a-bot-that-sends-a-message-if-more-than-x-time-has-passed)
    - [Run automatically as systemd service after boot](#run-automatically-as-systemd-service-after-boot)

YFT stands for Yahoo Finance + Telegram.

It's a Telegram bot that uses the [yfinance](https://github.com/ranaroussi/yfinance) library.

[Code](./src/bot.py) takes inspiration from this [tutorial](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot).

## Preparation

- Get an API token from "BotFather", see Telegram docs.
- Set as environment variable: export `TELEGRAMTOKEN=<token>` or add to .env file.

## Start a responsive bot

```python
python src/reponsive.py
```

## Start a bot that sends a message if more than X time has passed

```python
python src/periodic.py
```

### Run automatically as systemd service after boot

Modify 'User' and 'ExecStart' below and save as `/etc/systemd/system/yftbot.service`.

```raw
[Unit]
Description=Yahoo Finance Telegram Bot
After=network.target
After=systemd-user-sessions.service
After=network-online.target

[Service]
User=###
Type=forking
ExecStart=/path/to/venv/bin/python /path/to/src/periodic.py
TimeoutSec=500

[Install]
WantedBy=multi-user.target
```

Then run, as root:

```bash
systemctl start yftbot.service
systemctl stop yftbot.service
# Run after boot:
systemctl enable yftbot.service
```
