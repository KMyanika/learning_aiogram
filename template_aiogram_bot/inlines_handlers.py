from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def ikb_forvard_id(mess):
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Переслать сообщение', switch_inline_query=mess)]
    ])
    return ikb