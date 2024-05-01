import asyncio
import configparser
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
from aiogram.types import Message

from keyboards.user_keyboards import main_menu_keyboard
from messages.user_messages import main_menu_messages

config = configparser.ConfigParser()
config.read("setting/config.ini")
BOT_TOKEN = config["BOT_TOKEN"]["BOT_TOKEN"]

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    main_menu_key = main_menu_keyboard()

    document = FSInputFile('messages/image/1.png')
    await message.answer_photo(photo=document, caption=main_menu_messages,
                               reply_markup=main_menu_key,
                               parse_mode="HTML")


async def main() -> None:
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
