import asyncio
import os
import time
from pprint import pformat

import schedule
from credentials import TOKEN
from telegram.ext import ApplicationBuilder, ExtBot
from yf_track import basic_info


async def send_vwce_basic_info() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    bot: ExtBot = app.bot
    await bot.send_message(chat_id=os.environ['TELEGRAMCHATID'],
                           text=pformat(basic_info('VWCE.DE')))

def send_update():
    asyncio.run(send_vwce_basic_info())

if __name__ == '__main__':
    print("")
    schedule.every().day.at("17:03", "Europe/Amsterdam").do(send_update)
    while True:
        schedule.run_pending()
        time.sleep(10)
