import json

from aiogram import types, F
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import main_menu_keyboard
from services.services import save_bot_info
from system.dispatcher import ADMIN_USER_ID, dp
from system.dispatcher import bot
from system.dispatcher import router


class Form(StatesGroup):
    text = State()


# Загрузка информации из JSON-файла
def load_bot_info():
    with open("messages/main_menu_messages.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


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
    save_bot_info(bot_info, file_path="messages/main_menu_messages.json")  # Сохраняем информацию в JSON
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


@router.callback_query(F.data == "main_menu")
async def main_menu_handlers(callback_query: types.CallbackQuery):
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = main_menu_keyboard()

    data = load_bot_info()
    document = FSInputFile('messages/image/1.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


def main_menu_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(command_start_handler)
    dp.message.register(update_info)
    dp.message.register(edit_info)
    dp.message.register(main_menu_handlers)
