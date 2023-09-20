from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def ikb_forward_id(mess):
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Переслать сообщение', switch_inline_query=mess)]
    ])
    return ikb


def ikb_homework():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Задачи с ЕГЭ', callback_data='ege')],
        [InlineKeyboardButton(text='Задачи по теории Python', callback_data='python')],
        [InlineKeyboardButton(text='Сдать домашку', callback_data='homework')]
    ])
    return ikb


def ikb_Kontakts():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Моя визитка', url='t.me/yanikam22')]
    ])
    return ikb


def ikb_ege_homework():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1', callback_data='ege1'),
         InlineKeyboardButton(text='2', callback_data='ege2'),
         InlineKeyboardButton(text='3', callback_data='ege3'),
         InlineKeyboardButton(text='4', callback_data='ege4'),
         InlineKeyboardButton(text='5', callback_data='ege5')
         ],
        [InlineKeyboardButton(text='6', callback_data='ege6'),
         InlineKeyboardButton(text='7', callback_data='ege7'),
         InlineKeyboardButton(text='8', callback_data='ege8'),
         InlineKeyboardButton(text='9', callback_data='ege9'),
         InlineKeyboardButton(text='10', callback_data='ege10')
         ],
        [InlineKeyboardButton(text='11', callback_data='ege11'),
         InlineKeyboardButton(text='12', callback_data='ege12'),
         InlineKeyboardButton(text='13', callback_data='ege13'),
         InlineKeyboardButton(text='14', callback_data='ege14'),
         InlineKeyboardButton(text='15', callback_data='ege15')
         ],
        [InlineKeyboardButton(text='16', callback_data='ege16'),
         InlineKeyboardButton(text='17', callback_data='ege17'),
         InlineKeyboardButton(text='18', callback_data='ege18'),
         InlineKeyboardButton(text='19-21', callback_data='ege19'),
         InlineKeyboardButton(text='22', callback_data='ege22')
         ],
        [InlineKeyboardButton(text='23', callback_data='ege23'),
         InlineKeyboardButton(text='24', callback_data='ege24'),
         InlineKeyboardButton(text='25', callback_data='ege25'),
         InlineKeyboardButton(text='26', callback_data='ege26'),
         InlineKeyboardButton(text='27', callback_data='ege27')
         ],
    ])
    return ikb


def ikb_python_homework():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Тип данных, Базовая арифметика', callback_data='python1'),],
        [InlineKeyboardButton(text='Условные операторы, ветвление', callback_data='python2')],
        [InlineKeyboardButton(text='Циклы wile и for', callback_data='python3')],
        [InlineKeyboardButton(text='Тип коллекций списки (list)', callback_data='python4')],
        [InlineKeyboardButton(text='Строковой тип данных (str)', callback_data='python5')],
        [InlineKeyboardButton(text='Самописные функции и рекурсия', callback_data='python6')]
    ])
    return ikb

#def ikb_tasks_ege():
