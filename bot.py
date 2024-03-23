from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функция-обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот.")
# Функция-обработчик текстовых сообщений
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # Создание экземпляра Updater и передача токена вашего бота
    updater = Updater('7051166533:AAGcZYQzkNNnbYImXuen2HhC9GKMquDn7tU', use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчика команды /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Регистрация обработчика текстовых сообщений
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

# Обработчик команды /save_currency
def save_currency(update, context):
    # Отправляем сообщение с просьбой ввести название валюты
    update.message.reply_text('Введите название валюты')

# Обработчик текстового сообщения
def handle_text(update, context):
    # Получаем введенное пользователем название валюты
    currency_name = update.message.text
    # Сохраняем название валюты в контексте
    context.user_data['currency_name'] = currency_name
    # Отправляем сообщение с просьбой ввести курс валюты к рублю
    update.message.reply_text('Введите курс валюты к рублю')

# Обработчик текстового сообщения
def handle_text(update, context):
    # Получаем введенный пользователем курс валюты к рублю
    currency_rate = update.message.text
    # Сохраняем название валюты и ее курс в словарь
    currency_name = context.user_data['currency_name']
    context.user_data['currencies'][currency_name] = currency_rate
    # Отправляем сообщение об успешном сохранении
    update.message.reply_text(f'Курс валюты {currency_name} к рублю сохранен: {currency_rate}')

# Инициализация бота и добавление обработчиков
updater = Updater('7051166533:AAGcZYQzkNNnbYImXuen2HhC9GKMquDn7tU', use_context=True)
updater.dispatcher.add_handler(CommandHandler('save_currency', save_currency))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

# Запуск бота
updater.start_polling()
updater.idle()

