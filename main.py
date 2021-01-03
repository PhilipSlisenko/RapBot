import io
import logging
import time

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from config import config
from lyrics_generator import generate_lyrics
from mixer import mix_song
from tts import generate_speech_from_text

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Привет! Напиши мне начало песни, а я придумаю продолжение. Желательно 2+ строчки.')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Ты начни, а я продолжу.')


def rap_generator(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text("Ок, сейчас что-нибудь придумаю...")
    update.effective_chat.send_chat_action('typing')

    lyrics = generate_lyrics(update.message.text)

    update.message.reply_text(lyrics)

    update.effective_chat.send_chat_action('typing')
    time.sleep(0.5)
    update.message.reply_text("Eщё сведу по быстрому...")
    update.effective_chat.send_chat_action('record_audio')

    lyrics_audio_bytes = generate_speech_from_text(lyrics)

    mix = mix_song(lyrics_audio_bytes)
    with io.BytesIO(lyrics_audio_bytes) as f:
        update.message.reply_audio(f, title=update.message.text, )


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(config['TELEGRAM_API_KEY'], use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, rap_generator))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
