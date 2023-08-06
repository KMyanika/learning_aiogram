from aiogram import Bot, Dispatcher, executor, types
import os
import dotenv

import asyncio
from default_commands import *
from text_handlers import *

dotenv.load_dotenv()
token = os.getenv("API_TOKEN")
admin = int(os.getenv("ADMIN"))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'
handlers_help_command = {}


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    if message.chat.id == admin:
        await message.answer(text="Привет, админ")
    else:
        await message.answer(text=f"Привет, {message.from_user.username}")
        await bot.send_message(chat_id=admin,
                               text=f'#newuser: @{message.from_user.username}\n'
                                    f'ID: `{message.chat.id}`\n'
                                    f'[Написать сообщение](tg://user?id={message.chat.id})',     #todo спрятать текстовые сообщения в text_handlers
                               parse_mode=pm)


@dp.message_handler(commands=["getmyid"])  #todo на следующий урок попробовать добавить кнопку переслать сообщение
async def command_getmyid(message: types.Message):
    await message.answer(text=f"Ваш ID: `{message.chat.id}`",
                         parse_mode=pm)


@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await message.answer(text=ForUsers.push_command_help(message))
    handlers_help_command[message.chat.id] = 'H'




@dp.message_handler()
async def messages_handlers(message: types.Message):
    message.text = message.text.lower().strip()
    if message.text == 'контакты':
        pass  #todo создать сообщение с моими контактами

    elif any(x in message.text for x in ('#help', 'help', 'помощь')):
        await bot.send_message(chat_id=admin,
                               text=ForAdmin.push_help_handlers(message, message.text),
                               parse_mode=pm)
        await message.answer(text=ForUsers.push_help_handlers(message))

    else:
        if handlers_help_command[message.chat.id] == 'H':
            handlers_help_command[message.chat.id] = ''
            await bot.send_message(chat_id=admin,
                                   text=ForAdmin.push_help_handlers(message, message.text),
                                   parse_mode=pm)
            await message.answer(text=ForUsers.push_help_handlers(message))





async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())