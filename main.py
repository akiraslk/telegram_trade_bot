import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from flask import Flask
import threading
import asyncio

# ---------------- CONFIG ----------------
BOT_TOKEN = "8327778526:AAHtQPM5vPbZV_KpKy70pcoknjRlqJ9ewWY"  # replace locally

# ---------------- Flask Keepalive ----------------
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot running successfully!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=10000)

# ---------------- Telegram Bot ----------------
async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running 24/7 on Render!")

async def main_bot():
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))

    # Start polling
    await app.run_polling()

# ---------------- RUN BOTH ----------------
if __name__ == "__main__":
    # Start Flask server in separate thread
    threading.Thread(target=run_flask, daemon=True).start()

    # Run Telegram bot in async loop
    asyncio.run(main_bot())
