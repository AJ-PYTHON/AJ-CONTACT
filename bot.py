from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm AJ PYTHON's CONATCT bot. How can I help you?")

# Echo handler: Respond with the same text
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

if __name__ == "__main__":
    # Replace with your API token
    "BOT_TOKEN": {
            "description": "𝑬𝒏𝒕𝒆𝒓 𝒀𝒐𝒖𝒓 𝑩𝒐𝒕 𝑻𝒐𝒌𝒆𝒏",
            "required": true
        },
    # Create the application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    app.run_polling()
