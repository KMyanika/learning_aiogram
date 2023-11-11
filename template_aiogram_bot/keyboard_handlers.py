from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def kb_command_start_menu():
    kb = ReplyKeyboardMarkup(row_width= 2, resize_keyboard=True)
    kb.add(KeyboardButton('Контакты'),
           KeyboardButton('Отправить домашку'))
    return kb

def kb_cancel():
    kb = ReplyKeyboardMarkup(row_width= 2, resize_keyboard=True)
    kb.add(KeyboardButton('Отменить'))
    return kb