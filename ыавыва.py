import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Задаем токен бота
BOT_TOKEN = 'your_bot_token'

# Определяем функцию-обработчик для команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот, который может отправлять тебе твои же сообщения.")

# Определяем функцию-обработчик для текстовых сообщений
def echo(update, context):
    # Получаем текст сообщения
    message_text = update.message.text
    # Получаем ID чата, из которого пришло сообщение
    chat_id = update.message.chat_id
    # Отправляем копию сообщения обратно пользователю
    message_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    response = requests.post(message_url, data={'chat_id': chat_id, 'text': message_text})