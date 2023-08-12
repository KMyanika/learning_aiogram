from aiogram import Bot, Dispatcher, executor, types
import os
import dotenv

import asyncio
from default_commands import *
from text_handlers import *
from inlines_handlers import *
from keyboard_handlers import *

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
        await message.answer(text=f"Привет, {message.from_user.username}",
                             reply_markup=kb_command_start_menu())
        await bot.send_message(chat_id=admin,
                               text=ForAdmin.push_command_start(message),     #todo спрятать текстовые сообщения в text_handlers
                               parse_mode=pm)


@dp.message_handler(commands=["getmyid"])  #todo на следующий урок попробовать добавить кнопку переслать сообщение
async def command_getmyid(message: types.Message):
    await message.answer(text=ForUsers.push_command_getmyid(message),
                         parse_mode=pm,
                         reply_markup=ikb_forvard_id(ForUsers.push_command_getmyid(message)))


@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await message.answer(text=ForUsers.push_command_help(message))
    handlers_help_command[message.chat.id] = 'H'




@dp.message_handler()
async def messages_handlers(message: types.Message):
    get_message_bot = message.text.lower().strip()
    if get_message_bot == 'контакты':
        await message.answer(text=ForUsers.push_button_contacts(message),
                             parse_mode=pm,
                             disable_web_page_preview=True)
        await bot.send_contact(chat_id=message.chat.id,
                               phone_number=79044920200,
                               first_name='Янина',
                               last_name='Кавшевич-Матусевич',
                               protect_content=True)

    elif any(x in get_message_bot for x in ('#help', 'help', 'помощь')):
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