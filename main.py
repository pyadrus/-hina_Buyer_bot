import asyncio
import configparser
import json
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile
from aiogram.types import Message

from keyboards.user_keyboards import main_menu_keyboard

config = configparser.ConfigParser()
config.read("setting/config.ini")
BOT_TOKEN = config["BOT_TOKEN"]["BOT_TOKEN"]

dp = Dispatcher()


# Загрузка информации из JSON-файла
def load_bot_info():
    with open("messages/main_menu_messages.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


# Сохранение информации в JSON-файл
def save_bot_info(data):
    with open("messages/main_menu_messages.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


ADMIN_USER_ID = 535185511

router = Router()
dp.include_router(router)


class Form(StatesGroup):
    text = State()


# Обработчик команды /edit (только для админа)
@router.message(Command("edit"))
async def edit_info(message: Message, state: FSMContext):
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Form.text)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Form.text)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info)  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    main_menu_key = main_menu_keyboard()

    document = FSInputFile('messages/image/1.png')
    data = load_bot_info()
    await message.answer_photo(photo=document, caption=data,
                               reply_markup=main_menu_key,
                               parse_mode="HTML")


async def main() -> None:
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
