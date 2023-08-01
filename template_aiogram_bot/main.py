from aiogram import Bot, Dispatcher, executor, types
import os
import dotenv

import asyncio
from default_commands import *

dotenv.load_dotenv()
token = os.getenv("API_TOKEN")
admin = int(os.getenv("ADMIN"))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    if message.chat.id == admin:
        await message.answer(text="Привет, админ")
    else:
        await message.answer(text=f"Привет, {message.from_user.username}")
        await bot.send_message(chat_id=admin,
                               text=f'#newuser: @{message.from_user.username}\n'
                                    f'ID: `{message.chat.id}`\n'
                                    f'[Написать сообщение](tg://user?id={message.chat.id})',
                               parse_mode=pm)


@dp.message_handler(commands=["getmyid"])
async def command_getmyid(message: types.Message):
    await message.answer(text=f"Ваш ID: `{message.chat.id}`",
                         parse_mode=pm)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)



async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())