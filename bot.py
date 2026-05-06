from telegram import Update
from telegram.ext import ApplicationBuilder , MessageHandler , filters , ContextTypes
from process_embed import inference,rag_pipeline
import joblib
BOT_TOKEN = "your_new_telegram_token_here"

# def rag_pipeline(query):
#     answer = "This will be your RAG answer"

#     return answer


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_question = update.message.text

    answer = rag_pipeline(user_question)

    await update.message.reply_text(answer)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Bot running...")

app.run_polling()