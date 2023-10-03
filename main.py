import asyncio
import logging
from bot import bot, dp


from handlers import (start_router,
                      # echo_router,
                      shop_router,
                      # questions_router
                      )
from aiogram.types import BotCommand


async def main():
    # bot.set_my_commands(
    #     BotCommand(command="start", description="Начало"),
    #     BotCommand(command="info", description="Получи информацию о себе"),
    #     BotCommand(command="shop", description="Наш магазин"),
    #     BotCommand(command="pic", description="Получить картинку")
    # )
    dp.include_router(start_router)
    dp.include_router(shop_router)
    # dp.include_router(questions_router)
    #
    # dp.include_router(echo_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

# import asyncio
# from dotenv import load_dotenv
#
# import random
# import os
# from os import getenv
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
#
# load_dotenv()
# token = getenv("BOT_TOKEN")
# bot = Bot(token=token)
# dp = Dispatcher()
#
#
#
#
#
# @dp.message(Command("photo"))
# async def send_random_picture(message: types.Message):
#     images_folder = "images/"
#     images = [f for f in os.listdir(images_folder) if f.endswith((".jpg", ".jpeg", ".png"))]
#     if images:
#         random_image = random.choice(images)
#         file = types.FSInputFile(images_folder + random_image)
#         await message.answer_photo(file)
#     else:
#         await message.answer("В папке с картинками нет подходящих файлов.")
#
#
# @dp.message(Command("myinfo"))
# async def my_info(message: types.Message):
#     user_id = message.from_user.id
#     first_name = message.from_user.first_name
#     username = message.from_user.username
#
#     info_message = f"Ваш ID: {user_id}\nИмя: {first_name}\nUsername: @{username}"
#     await message.answer(info_message)
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     asyncio.run(main())