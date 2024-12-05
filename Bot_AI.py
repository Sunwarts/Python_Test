from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext, CallbackQueryHandler
from openai import OpenAI

# Установка вашего API ключа (key_python1 - https://platform.openai.com/ )
api_key = 'api_key'
client = OpenAI(api_key=api_key)

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton('Начать', callback_data='start_chat')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Нажмите на кнопку "Начать", чтобы начать диалог.', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == "start_chat":
        query.edit_message_text(text="Напишите сообщение, чтобы начать диалог")


def chat_with_ai(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text

    if "chat_history" not in context.user_data:
        context.user_data['chat_history'] = []

    context.user_data['chat_history'].append({"role": "user", "content": user_input})

    # Отправляем временное сообщение
    temp_message = update.message.reply_text("Обрабатываем ваш запрос...")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=context.user_data['chat_history'],
        max_tokens=4000
    )

    ai_response = response.choices[0].message.content

    context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                  message_id=temp_message.message_id,
                                  text=ai_response)

    if len(context.user_data['chat_history']) >50:
        context.user_data['chat_history'] = context.user_data['chat_history'] [-50:]

# Токен вашего бота (t.me/My_PythonAI_bot)
TELEGRAM_TOKEN = "token from telegram"

def main():
    
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_with_ai))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
