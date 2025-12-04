import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from flask import Flask
import threading

BOT_TOKEN = "8327778526:AAHtQPM5vPbZV_KpKy70pcoknjRlqJ9ewWY"

# ---------------- Flask Keepalive Server -------------------

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot running successfully!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# ---------------- Telegram Bot Logic -----------------------

async def start(update: Update, context):
    await update.message.reply_text("Bot is running 24/7 on Render!")

def main():
    logging.basicConfig(level=logging.INFO)

    telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()

    telegram_app.add_handler(CommandHandler("start", start))

    # Start Flask server in separate thread
    threading.Thread(target=run_flask).start()

    telegram_app.run_polling()

if __name__ == "__main__":
    main()
