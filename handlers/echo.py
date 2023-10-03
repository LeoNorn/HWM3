from aiogram import types, Router, F
from aiogram.filters import Command
from keyboards.KB import kb_shop


echo_router = Router()


@echo_router.message(Command("myinfo1"))
async def my_info():
    pass
