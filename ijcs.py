from typing import Text
from telegram import Update, ForceReply , BotCommand
 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext 

Token = "6441751594:AAHlslZgyHSP3luQjvuxzmUXOfPGynqFmTg"



async def start(update: Update, _: CallbackContext) -> None:
   await update.message.reply_text("Hello! Welcome to IJCS where you can find relevant jobs.")


async def help(update: Update, _: CallbackContext) -> None:
    message = """
    /start -> Welcome to IJCS
    /help -> This message will help you get started with us
    /content -> Here you can find the content of job posts
    /contact -> Here you can contact our team for any queries, assistance, and suggestions
    """
    await update.message.reply_text(message)


async def contact(update: Update, _: CallbackContext) -> None:
    message = """
    /call -> 0934094406
    /email -> ijcs@gmail.com
    /telegram -> @IJCSofficial
    """
    await update.message.reply_text(message)


async def content(update: Update, _: CallbackContext) -> None:
   await update.message.reply_text("IJCS provides relevant and trustworthy information about new job openings.")


 

def run_bot(update: Update, _: CallbackContext) -> None:
    replica = update.message.text
    # Process the user input (e.g., call a function to generate a response)
    answer = process_user_input(replica)  # Replace with your actual logic
    update.message.reply_text(answer)

def main() -> None:
    application = Application.builder().token(Token).build()

    # Add your command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("content", content))
    application.add_handler(MessageHandler(Text and BotCommand, run_bot))

    # Run the bot
    application.run_polling(1.0)

if __name__ == "__main__":
    main()
