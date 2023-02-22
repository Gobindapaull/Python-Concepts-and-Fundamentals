import time
import logging
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = ""
MSG = "Random Text by you {}"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])

async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f'{user_full_name}, How are you doing today!') #first
    for i in range(10):
        time.sleep(2)
        await bot.send_message(user_id, MSG.format(user_name)) #second

if __name__ == "__main__":
    executor.start_polling(dp)

