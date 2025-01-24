from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Команда /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я бот для игры Ash & Abyss.')

# Основная функция
def main():
    # Вставь сюда свой токен
    token = 'ТВОЙ_ТОКЕН'
    updater = Updater(token)

    # Регистрация команд
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()