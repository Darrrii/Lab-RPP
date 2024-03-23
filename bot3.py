from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Определение состояний для обработчика
CURRENCY, RATE, CONVERT_CURRENCY, CONVERT_AMOUNT = range(4)

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
    context.user_data[context.user_data['currency']] = update.message.text
    update.message.reply_text('Курс валюты успешно сохранен.')
    return ConversationHandler.END

# Функция для начала конвертации валюты
def convert_currency(update, context):
    update.message.reply_text('Введите название валюты:')
    return CONVERT_CURRENCY

# Функция для сохранения названия валюты и перехода к вводу суммы
def input_currency_for_conversion(update, context):
    context.user_data['currency'] = update.message.text
    update.message.reply_text('Введите сумму в выбранной валюте:')
    return CONVERT_AMOUNT

# Функция для конвертации суммы в рубли
def perform_conversion(update, context):
    currency = context.user_data['currency']
    amount = float(update.message.text)
    if currency in context.user_data:  # Проверяем, сохранен ли курс выбранной валюты
        rate = float(context.user_data[currency])
        converted_amount = amount * rate
        update.message.reply_text(f'{amount} {currency} = {converted_amount} RUB')
    else:
        update.message.reply_text('Курс выбранной валюты не найден.')
    return ConversationHandler.END

# Функция для обработки команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот. Чем могу помочь?")

def main():
    # Инициализация бота
    updater = Updater('7051166533:AAGcZYQzkNNnbYImXuen2HhC9GKMquDn7tU', use_context=True)
    dp = updater.dispatcher

    # Создание обработчика команды /save_currency
    conv_handler_save = ConversationHandler(
        entry_points=[CommandHandler('save_currency', save_currency)],
        states={
            CURRENCY: [MessageHandler(Filters.text, input_currency)],
            RATE: [MessageHandler(Filters.text, input_rate)]
        },
        fallbacks=[]
    )

    # Создание обработчика команды /convert
    conv_handler_convert = ConversationHandler(
        entry_points=[CommandHandler('convert', convert_currency)],
        states={
            CONVERT_CURRENCY: [MessageHandler(Filters.text, input_currency_for_conversion)],
            CONVERT_AMOUNT: [MessageHandler(Filters.text, perform_conversion)]
        },
        fallbacks=[]
    )

    # Регистрация обработчиков
    dp.add_handler(conv_handler_save)
    dp.add_handler(conv_handler_convert)
    dp.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()