from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from yft_bot.credentials import TOKEN
from yft_bot.bot import start, help, track, regular_text

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    track_handler = CommandHandler('track', track)
    text_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), regular_text)
    app.add_handler(start_handler)
    app.add_handler(help_handler)
    app.add_handler(track_handler)
    app.add_handler(text_handler)
    app.run_polling()
