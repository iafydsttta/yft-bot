import asyncio
import os
from pprint import pformat
import time

import schedule
from telegram.ext import ApplicationBuilder, ExtBot

from yf_track import basic_info
from credentials import TOKEN


async def send_vwce_basic_info() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    bot: ExtBot = app.bot
    await bot.send_message(chat_id=os.environ['TELEGRAMCHATID'],
                           text=pformat(basic_info('VWCE.DE')))

def send_update():
    asyncio.run(send_vwce_basic_info())

if __name__ == '__main__':
    print("")
    schedule.every().day.at("16:55", "Europe/Amsterdam").do(send_update)
    while True:
        schedule.run_pending()
        time.sleep(10)
