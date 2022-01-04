from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from bot_token import token_var
import os, random

# Define a few command handlers. These usually take the two arguments update and
# context.

def button(update: Update, context: CallbackContext):
    callback_logging(update)
    query = update.callback_query
    query.answer()

    query.edit_message_text(query.data)
    if query.data == "WEIQI 1000 PROBLEMS":
        keyboard = [[InlineKeyboardButton("CGP 1.1 - Making Life", callback_data='CGP 1.1 - Making Life')], [InlineKeyboardButton("CGP 1.2 - Destroying Eyes", callback_data='CGP 1.2 - Destroying Eyes')], [InlineKeyboardButton("CGP 1.3 - Killing Eyes", callback_data='CGP 1.3 - Killing Eyes')], \
                    [InlineKeyboardButton("CGP 1.4 - Semeai", callback_data='CGP 1.4 - Semeai')], [InlineKeyboardButton("CGP 1.5 - Seki", callback_data='CGP 1.5 - Seki')], [InlineKeyboardButton("CGP 1.6 - Vital Point", callback_data='CGP 1.6 - Vital Point')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.callback_query.message.reply_text('Please select the lesson from the pack', reply_markup=reply_markup)
    elif query.data == "CGP 1.1 - Making Life" or \
         query.data == "CGP 1.2 - Destroying Eyes" or \
         query.data == "CGP 1.3 - Killing Eyes" or \
         query.data == "CGP 1.4 - Semeai" or \
         query.data == "CGP 1.5 - Seki" or \
         query.data == "CGP 1.6 - Vital Point" or \
         query.data == "CGP 1.7 - Go Theory" or \
         query.data == "CGP 1.8 - Common Corner Position" or \
         query.data == "CGP 1.9 - Making Ko" or \
         query.data == "CGP 1.10 - Interesting Unusual Problem" or \
         query.data == "CGP 2.1 - Ladder" or \
         query.data == "CGP 2.2 - Cut" or \
         query.data == "CGP 2.3 - Net" or \
         query.data == "CGP 2.4 - Hane" or \
         query.data == "CGP 2.5 - Wedge" or \
         query.data == "CGP 2.6 - Diagonal" or \
         query.data == "CGP 2.7 - Bridge Under" or \
         query.data == "CGP 2.7 - Bridge Under" or \
         query.data == "CGP 2.9 - Pincer & Clamp" or \
         query.data == "CGP 2.10 - Descent and Stand" or \
         query.data == "CGP 2.11 - Vital Point 2" or \
         query.data == "CGP 2.12 - Throw in" or \
         query.data == "CGP 2.13 - Two-stone Edge Squeeze" or \
         query.data == "CGP 2.14 - Double Shortage of Liberties" or \
         query.data == "CGP 2.15 - Under the Stones":
        problem = random.choice(os.listdir("../sgfs/WEIQI 1000 PROBLEMS/" + query.data)).split(".")
        #print("{} {} {} at {}: {}".format(update.callback_query.from_user.username, update.callback_query.from_user.first_name, update.callback_query.from_user.id, update.callback_query.message.date, update.callback_query.data))
        print(query.data + " : " + ''.join(problem))
        #print('../sgfutils-0.25/sgftopng -nonrs ' + '"' + '../sgfs/WEIQI 1000 PROBLEMS/' + query.data + '/' + problem[0] + '.png' + '"' + ' < ' + '"' + '../sgfs/WEIQI 1000 PROBLEMS/' + query.data + '/' + problem[0] + '.sgf' + '"')
        os.system('../sgfutils-0.25/sgftopng -coord -nonrs ' + '"' + '../sgfs/WEIQI 1000 PROBLEMS/' + query.data + '/' + problem[0] + '.png' + '"' + ' < ' + '"' + '../sgfs/WEIQI 1000 PROBLEMS/' + query.data + '/' + problem[0] + '.sgf' + '"')

        photo = open("../sgfs/WEIQI 1000 PROBLEMS/" + query.data + "/" + problem[0] + ".png", 'rb')
        update.callback_query.message.reply_photo(photo)



def get_list_of_packs(update: Update, context: CallbackContext):
    logging(update)
    keyboard = [[InlineKeyboardButton("WEIQI 1000 PROBLEMS", callback_data='WEIQI 1000 PROBLEMS'), InlineKeyboardButton("smth else", callback_data='smth else')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please select the problems pack',reply_markup=reply_markup)

def check_admin_id(update: Update):
    pass

def callback_logging(update: Update):
    print("{} {} {} at {}: {}".format(update.callback_query.from_user.username, update.callback_query.from_user.first_name, update.callback_query.from_user.id, update.callback_query.message.date, update.callback_query.data))

def logging(update: Update):
    print("{} {} {} at {}: {}".format(update.message.from_user.username, update.message.from_user.first_name, update.message.from_user.id, update.message.date , update.message.text))

def start(update: Update, context: CallbackContext):
    logging(update)
    #user = update.effective_user
    #update.message.reply_markdown_v2(
    #    fr'Hi {user.mention_markdown_v2()}\!', reply_markup=ForceReply(selective=True),)
    update.message.reply_text("Hello!")

def help_command(update: Update, context: CallbackContext):
    logging(update)
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def get_problem(update: Update, context: CallbackContext):
    logging(update)
    global chosen_file
    chosen_file = random.choice(os.listdir("./sgfs/parsed_incomplete/"))
    #command = "./sgfutils-0.25/sgftopng ./parsed_sgfs/" + chosen_file + ".png < ./sgfs/" + chosen_file + ".sgf"
    #os.system(command)
    photo = open("./sgfs/parsed_incomplete/" + chosen_file, 'rb')
    update.message.reply_photo(photo)

def get_answer(update: Update, context: CallbackContext):
    logging(update)
    photo = open("./sgfs/parsed_right_answers/" + chosen_file, 'rb')
    update.message.reply_photo(photo)

def echo(update: Update, context: CallbackContext):
    logging(update)
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
    dispatcher.add_handler(CommandHandler("get_list_of_packs", get_list_of_packs))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=button))

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
