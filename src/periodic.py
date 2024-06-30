import asyncio
import os
import time

import schedule
import telegram
from credentials import TOKEN
from telegram.ext import ApplicationBuilder, ExtBot
from yf_track import dict_to_markdown, get_cached_tracker_info


async def send_vwce_basic_info() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    bot: ExtBot = app.bot
    message = dict_to_markdown(get_cached_tracker_info("VWCE.DE"))
    print(message)
    await bot.send_message(
        chat_id=os.environ["TELEGRAMCHATID"],
        text=message,
        parse_mode=telegram.constants.ParseMode.MARKDOWN_V2,
    )


def send_update():
    asyncio.run(send_vwce_basic_info())


if __name__ == "__main__":
    # schedule.every().day.at("17:13", "Europe/Amsterdam").do(send_update)
    # schedule.every().minute.do(send_update)
    schedule.every(5).seconds.do(send_update)
    # schedule.every().second.do(send_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
