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
hw = int(os.getenv("HOMEWORK"))

bot = Bot(token)
dp = Dispatcher(bot)
pm = 'Markdown'
handlers_help_command = {}
actions = {}

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    if message.chat.id == admin:
        await message.answer(text=ForAdmin.push_command_start(),
                             reply_markup=kb_command_start_menu())
    else:
        await message.answer(text=ForUsers.push_command_start(message),
                             reply_markup=kb_command_start_menu())
        await bot.send_message(chat_id=admin,
                               text=ForAdmin.push_if_use_command_start(message),
                               parse_mode=pm)


@dp.message_handler(commands=['homework'])
async def command_homework(message: types.Message):
    await message.answer(text='Выберите нужную кнопку',
                         reply_markup=ikb_homework())


@dp.message_handler(commands=["getmyid"])
async def command_getmyid(message: types.Message):
    await message.answer(text=ForUsers.push_command_getmyid(message),
                         parse_mode=pm,
                         reply_markup=ikb_forward_id(ForUsers.push_command_getmyid(message)))


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
                               protect_content=True,
                               reply_markup=ikb_Kontakts())

    elif any(x in get_message_bot for x in ('#help', 'help', 'помощь')):
        await bot.send_message(chat_id=admin,
                               text=ForAdmin.push_help_handlers(message, message.text),
                               parse_mode=pm)
        await message.answer(text=ForUsers.push_help_handlers(message))
    elif get_message_bot == 'отменить':
        await message.answer(text='Команда успешно отменена',
                             reply_markup=kb_command_start_menu())
    elif get_message_bot == 'отправить домашку':
        await message.answer(text=ForUsers.push_take_homework(message))
        actions[message.chat.id] = 'take_home'

    else:
        if handlers_help_command.get(message.chat.id) == 'H':
            handlers_help_command[message.chat.id] = ''
            await bot.send_message(chat_id=admin,
                                   text=ForAdmin.push_help_handlers(message, message.text),
                                   parse_mode=pm)
            await message.answer(text=ForUsers.push_help_handlers(message))

        elif actions.get(message.chat.id) == 'take_home':
            await message.answer(text=ForUsers.push_succesful_take_homework(message))
            await bot.send_message(chat_id=hw,
                                    text=ForAdmin.push_student_send_homework(message,
                                                                            message.from_user.first_name,
                                                                            message.text))


@dp.callback_query_handler()
async def callback_handlers(call: types.callback_query):
    if call.data == 'ege':
        await call.message.answer(text='Получите домашку', reply_markup=ikb_ege_homework())
    elif 'ege' in call.data:
        num = int(call.data[3:])
        await call.message.answer(text=ForUsers.push_homework_ege(call.message, num),
                                  parse_mode=pm,
                                  disable_web_page_preview=True)
        await bot.send_message(chat_id=hw,
                               text=ForAdmin.push_student_take_homework_ege(call.message, call.message.from_user.first_name, num),
                               parse_mode=pm,
                               disable_web_page_preview=True)
    elif call.data == 'python':
        await call.message.answer(text='Получите домашку', reply_markup=ikb_python_homework())
    elif 'python' in call.data:
        num = int(call.data[6:])
        await call.message.answer(text=ForUsers.push_homework_python(call.message, num),
                                  parse_mode=pm,
                                  disable_web_page_preview=True)
        await bot.send_message(chat_id=hw,
                               text=ForAdmin.push_student_take_homework_python(call.message, call.message.from_user.first_name, num),
                               parse_mode=pm,
                               disable_web_page_preview=True)
        #todo пофиксить штуку с именами, брать имена из базы данных

    elif call.data == 'homework':
        await call.message.answer(text=ForUsers.push_take_homework(call.message),
                                  reply_markup=kb_cancel())
        actions[call.message.chat.id] = 'take_home'





async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())