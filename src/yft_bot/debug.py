import asyncio
import os

from telegram.ext import (
    ApplicationBuilder,
    ExtBot,
)

from yft_bot.credentials import TOKEN


async def send_message_to_myself() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    bot: ExtBot = app.bot
    await bot.send_message(chat_id=os.environ['TELEGRAMCHATID'], text="Lorem Ipsum")

if __name__ == '__main__':
    asyncio.run(send_message_to_myself())
