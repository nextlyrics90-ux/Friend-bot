import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBSITE_LINK = os.getenv("WEBSITE_LINK", "https://hotAura786.blogspot.com")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"👋 Welcome to Friend Bot! Visit our website: {WEBSITE_LINK}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
