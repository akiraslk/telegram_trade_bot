import logging
import asyncio
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask

# ---------------- CONFIG ----------------
BOT_TOKEN = "8327778526:AAHtQPM5vPbZV_KpKy70pcoknjRlqJ9ewWY"  # Replace with your Telegram bot token

# ---------------- Flask Keepalive ----------------
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot running successfully!"

def run_flask():
    # Flask must run on 0.0.0.0 and port 10000 for Render
    flask_app.run(host="0.0.0.0", port=10000)

# ---------------- Telegram Bot Handlers ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Bot is running 24/7 on Render.\nUse /newtrade to start your pre-trade checklist."
    )

# ---------------- Telegram Bot Setup ----------------
async def main_bot():
    # Logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Create bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))

    # Start polling (async)
    await app.run_polling()

# ---------------- RUN BOTH ----------------
if __name__ == "__main__":
    # Start Flask server in separate daemon thread
    threading.Thread(target=run_flask, daemon=True).start()

    # Run Telegram bot in asyncio loop
    asyncio.run(main_bot())
