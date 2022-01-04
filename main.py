import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot_token import token_var
import os, random

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    #user = update.effective_user
    #update.message.reply_markdown_v2(
    #    fr'Hi {user.mention_markdown_v2()}\!', reply_markup=ForceReply(selective=True),)
    update.message.reply_text("Hello!")

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def get_problem(update: Update, context: CallbackContext) -> None:
    global chosen_file
    chosen_file = random.choice(os.listdir("./sgfs/parsed_incomplete/"))
    #command = "./sgfutils-0.25/sgftopng ./parsed_sgfs/" + chosen_file + ".png < ./sgfs/" + chosen_file + ".sgf"
    #os.system(command)
    photo = open("./sgfs/parsed_incomplete/" + chosen_file, 'rb')
    update.message.reply_photo(photo)

def get_answer(update: Update, context: CallbackContext) -> None:
    photo = open("./sgfs/parsed_right_answers/" + chosen_file, 'rb')
    update.message.reply_photo(photo)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token_var)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("get_problem", get_problem))
    dispatcher.add_handler(CommandHandler("get_answer", get_answer))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
