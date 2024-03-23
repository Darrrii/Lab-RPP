from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import logging

# Определение состояний для обработчика
CURRENCY, RATE = range(2)

# Функция для начала сохранения курса валюты
def save_currency(update, context):
    update.message.reply_text('Введите название валюты:')
    return CURRENCY

# Функция для сохранения названия валюты и перехода к вводу курса
def input_currency(update, context):
    context.user_data['currency'] = update.message.text
    update.message.reply_text('Введите курс валюты к рублю:')
    return RATE

# Функция для сохранения курса валюты и завершения сохранения
def input_rate(update, context):
    context.user_data['rate'] = update.message.text
    currency = context.user_data['currency']
    rate = context.user_data['rate']
    update.message.reply_text(f'Сохранено: {currency} - {rate} RUB')
    return ConversationHandler.END

# Функция для обработки команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот. Чем могу помочь?")

def main():
    # Инициализация бота
    updater = Updater('7051166533:AAGcZYQzkNNnbYImXuen2HhC9GKMquDn7tU', use_context=True)
    dp = updater.dispatcher

    # Создание обработчика команды /save_currency
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('save_currency', save_currency)],
        states={
            CURRENCY: [MessageHandler(Filters.text, input_currency)],
            RATE: [MessageHandler(Filters.text, input_rate)]
        },
        fallbacks=[]
    )

    # Регистрация обработчика
    dp.add_handler(conv_handler)

    # Регистрация обработчика команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()