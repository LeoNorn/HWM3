from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Наш сайт", callback_data='start_shop'),
                          InlineKeyboardButton(text="наш магазин", callback_data='start_shop')],
                         [InlineKeyboardButton(text="О нас", callback_data="about")]]
    )
    await message.answer("Привет, друзья", reply_markup=kb)

    # await message.answer("Привет, друзья", reply_markup=await kb_shop())


@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await  callback.answer()
    await callback.message.answer("О нас")
