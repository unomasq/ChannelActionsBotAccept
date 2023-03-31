import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ChatPermissions
from aiogram.dispatcher.filters import Command, ChatTypeFilter


bot = Bot(token='<YOUR-BOT-TOKEN-HERE>')
dp = Dispatcher(bot)

# Enable logging
logging.basicConfig(level=logging.INFO)


@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    user_id=update.from_user.id
    await bot.send_message(user_id, 'Реклама')
    #тут можно добавить пользователя в бд для дальнейших рассылок
    await update.approve() #.decline() если отклоняем


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
