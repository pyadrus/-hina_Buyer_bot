import asyncio
import configparser
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.user_keyboards import main_menu_keyboard

config = configparser.ConfigParser()
config.read("setting/config.ini")
BOT_TOKEN = config["BOT_TOKEN"]["BOT_TOKEN"]

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    main_menu_key = main_menu_keyboard()
    await message.answer(text="Hello!", reply_markup=main_menu_key)


async def main() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
