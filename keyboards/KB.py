from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def kb_shop():
    button1 = InlineKeyboardButton(text='о нас', callback_data='start_about')
    button2 = InlineKeyboardButton(text='наш магазин', callback_data='start_shop')
    markup = InlineKeyboardMarkup()
    markup.add(button1, button2)
    return markup
