import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "MorpheusBot is running."

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Telegram bot token
TOKEN = os.getenv('BOT_TOKEN')

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome. Morpheus sees all.")

def main():
    # Start Flask app in a separate thread
    Thread(target=run_flask).start()

    # Start Telegram bot
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
