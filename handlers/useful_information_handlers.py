from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import main_menu_selection_keyboard
from services.services import load_bot_info_services_and_prices
from services.services import save_bot_info
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "useful_information")
async def useful_information_handlers(callback_query: types.CallbackQuery):
    """📚 Полезная информация"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    data = load_bot_info_services_and_prices(file_path="messages/useful_information_messages.json")
    main_menu_key = main_menu_selection_keyboard()

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_key
    )


class Foruseful_information(StatesGroup):
    text_useful_information = State()


# Обработчик команды /edit_useful_information (только для админа)
@router.message(Command("edit_useful_information"))
async def edit_useful_information(message: Message, state: FSMContext):
    """Редактирование информации: 📚 Полезная информация"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Foruseful_information.text_useful_information)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Foruseful_information.text_useful_information)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info,
                  file_path="messages/useful_information_messages.json")  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def useful_information_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(useful_information_handlers)  # Добавляем обработчик 📚 Полезная информация
    dp.message.register(edit_useful_information)  # Редактирование информации: 📚 Полезная информация
    # скотч
