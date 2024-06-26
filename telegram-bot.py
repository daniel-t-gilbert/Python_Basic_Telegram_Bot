from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! Welcome to Daniel's new Bot. Click /help to view available options")

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome to Daniel's Bot
    /help -> This message
    /about -> About this bot
    /english -> Daniel's fav English song
    /malayalam -> Daniel's fav Malayalam song
    /hindi -> Daniel's fav Hindi song
    /contact -> contact information 
    """)

async def about(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Just a sample bot created by Daniel to showcase some of Daniel's fav songs")

async def english(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("English Song Link: https://youtu.be/UtF6Jej8yb4?si=vvAR1ayX26_FS8S5")

async def malayalam(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Malayalam Song Link: https://youtu.be/O_ZIs4p14Fo?si=qbG6hxVjrX77uFO6")

async def hindi(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hindi Song Link: https://youtu.be/RyUjINMGDl0?si=7MoqZpcfCIpzwb9K")

async def contact(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("You can contact me on my official email: danieltgilbert03@gmail.com")

async def handle_message(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f"You said {update.message.text}, use the commands using /")

def main() -> None:
    # Replace "YOUR_TELEGRAM_BOT_TOKEN" with your bot's token
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('about', about))
    application.add_handler(CommandHandler('english', english))
    application.add_handler(CommandHandler('malayalam', malayalam))
    application.add_handler(CommandHandler('hindi', hindi))
    application.add_handler(CommandHandler('contact', contact))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
