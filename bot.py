from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот для игры Ash & Abyss.')

# Основная функция
def main():
    # Вставь сюда свой токен
    token = 7721415697:AAHg2P1-8N7YleIfNC8wZqUyB2znDHCeTAQ

    # Создаём приложение и передаём токен
    application = Application.builder().token(token).build()

    # Регистрируем команду /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()