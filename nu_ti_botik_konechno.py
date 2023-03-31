import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
import asyncio
import random
import requests
from bs4 import BeautifulSoup as b
import random
import aiohttp

API_TOKEn = '5779005200:AAFjOjudoufIehZYZaF9ZQspfSVi_eaXz_s'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEn)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


def fetch_anecdote():
    url = 'https://www.anekdot.ru/random/anekdot/'
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anecdotes = soup.find_all('div', class_='text')
    anecdotes = [c.text for c in anecdotes]
    random_anecdote = random.choice(anecdotes)
    return random_anecdote


# Настройка кнопок
main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.add("сигма", "анекдоты")
back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_markup.add("назад")


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Выбери одну из кнопок. Но если ты хочешь получить гифку по запросу, то воспользуйся /gif + request. Пример: /gif hello", reply_markup=main_markup)


@dp.message_handler(lambda message: message.text == 'сигма')
async def send_gif(message: types.Message):
    await message.reply_animation("https://i.gifer.com/FPm.gif", reply_markup=back_markup)


@dp.message_handler(lambda message: message.text == 'анекдоты')
async def send_anecdote(message: types.Message):
    anecdote = fetch_anecdote()
    await bot.send_message(message.chat.id, anecdote)


@dp.message_handler(lambda message: message.text == 'назад')
async def go_back(message: types.Message):
    await message.reply("Возвращаемся...", reply_markup=main_markup)


GIPHY_API_URL = "http://api.giphy.com/v1/gifs/search"
GIPHY_API_KEY = "hnFZ817FOjpoNHk5ueQrIau9uWYWXfR4"


# Функция, которая будет создавать и отправлять гифки
async def send_gif(message: types.Message, search_term: str) -> None:
    # Отправляем запрос к API сервиса Giphy
    async with aiohttp.ClientSession() as session:
        async with session.get(
                GIPHY_API_URL,
                params={
                    "api_key": GIPHY_API_KEY,
                    "q": search_term,
                    "limit": 10,  # количество результатов
                    "offset": random.randint(0, 50),  # смещение
                },
        ) as response:
            data = await response.json()

    # Получаем ссылку на случайную гифку из результатов
    gif_url = random.choice(data["data"])["images"]["downsized_medium"]["url"]

    # Отправляем гифку пользователю
    await bot.send_document(message.chat.id, gif_url)


# Хэндлер на команду /gif
@dp.message_handler(commands=["gif"])
async def cmd_gif(message: types.Message) -> None:
    # Получаем текст после команды /gif
    search_term = message.text.split(maxsplit=1)[1]

    # Создаем и отправляем гифку
    await send_gif(message, search_term)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
