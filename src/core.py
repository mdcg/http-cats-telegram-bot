from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import BASE_API_URL, TELEGRAM_TOKEN


def start(bot, update):
    response_message = "=^._.^="
    bot.send_message(chat_id=update.message.chat_id, text=response_message)


def http_cats(bot, update, args):
    bot.sendPhoto(chat_id=update.message.chat_id, photo=BASE_API_URL + args[0])


def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(chat_id=update.message.chat_id, text=response_message)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("http", http_cats, pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    print("press CTRL + C to cancel.")
    main()
