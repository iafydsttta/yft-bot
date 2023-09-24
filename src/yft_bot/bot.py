import logging
import pprint

from telegram import Update
from telegram.ext import ContextTypes

from yft_bot.yf_track import basic_info

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Reduce relatively spammy httpx logging
logging.getLogger('httpx').setLevel(logging.WARNING)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
        text="This command does not do anything really. I'm a bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # all lines after first will be indented
    text =  \
        """
            Commands

            /start      :: Initialize chat with this bot
            /help       :: Show this help message
            /track      :: Track a ticker, like "VWCE.DE"
        """

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ticker = "VWCE.DE"
    try:
        info = basic_info(ticker)
        message = pprint.pformat(info)
    except Exception as e:
        message = f"Exception while fetching info for Ticker {ticker}.\nException: {e}"

    await context.bot.send_message(chat_id=update.effective_chat.id,
        text=message)


async def regular_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.debug(f"{update.effective_chat.id=}")
    await context.bot.send_message(chat_id=update.effective_chat.id,
        text="No smart LLM responses here. All hardcoded goodness.")

    # just echo:
    # await context.bot.send_message(chat_id=update.effective_chat.id,
    #                                text=update.message.text)
