from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

shop_router = Router()


@shop_router.callback_query(F.data == "start_shop")
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Манга"),
            KeyboardButton(text="Книги"),
            KeyboardButton(text="Комиксы")
        ]]
    )
    await message.answer("Выберите категорию ниже:")


@shop_router.message(F.text == "Манга")
async def show_manga(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Список манги в нашем магазине:",reply_markup=kb)