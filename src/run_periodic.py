import asyncio
import os
import time
from datetime import datetime, timedelta
from pathlib import Path

import telegram
from httpx import NetworkError
from telegram.ext import ApplicationBuilder, ExtBot

from src.lib.credentials import TOKEN
from src.lib.yahoo_finance.trackers import dict_to_markdown, get_cached_tracker_info

CACHE_DIR = Path(os.path.expanduser("~/.cache/yft-bot/"))
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FILE = CACHE_DIR / "last_message_sent.log"
NETWORK_DELAY_SECONDS = 120
SEND_AFTER_X_DAYS = 4


async def send_vwce_basic_info() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    bot: ExtBot = app.bot
    message = dict_to_markdown(get_cached_tracker_info("VWCE.DE"))

    print(message)

    try:
        _ = await bot.send_message(
            chat_id=os.environ["TELEGRAMCHATID"],
            text=message,
            parse_mode=telegram.constants.ParseMode.MARKDOWN_V2,
        )
        serialized_date = datetime.now().strftime(DATE_FORMAT)

        # Log timestamp
        with open(LOG_FILE, "w") as f:
            f.write(serialized_date)

    except NetworkError as e:
        print(f"Could not send message: {e}")


def send_update():
    asyncio.run(send_vwce_basic_info())


if __name__ == "__main__":
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as f:
            line = f.readline()
        last_message_time = datetime.strptime(line, DATE_FORMAT)
        print(f"{last_message_time=}")
        time_since = datetime.now() - last_message_time
        print(f"{time_since=}")
        if time_since > timedelta(days=SEND_AFTER_X_DAYS):
            # Give network some time to come online after boot
            time.sleep(NETWORK_DELAY_SECONDS)
            send_update()

    # print current date/time in local time Amsterdam
    print(datetime.now().strftime(DATE_FORMAT))
