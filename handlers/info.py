from aiogram import types, Router
from aiogram.filters import Command


info_router = Router()


@info_router.message(Command("myinfo"))
async def my_info():
    pass
