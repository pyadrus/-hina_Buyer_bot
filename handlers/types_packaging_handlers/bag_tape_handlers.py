from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import tapes_packing_keyboard_back
from services.services import load_bot_info_services_and_prices, save_bot_info
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "bag_tape")
async def bag_tape_handlers(callback_query: types.CallbackQuery):
    """Мешок + скотч"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    data = load_bot_info_services_and_prices(file_path="messages/types_packaging_messages/bag_tape_messages.json")
    main_menu_key = tapes_packing_keyboard_back()

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_key
    )


class Formbag_tape(StatesGroup):
    text_bag_tape = State()


# Обработчик команды /edit_bag_tape (только для админа)
@router.message(Command("edit_bag_tape"))
async def edit_bag_tape(message: Message, state: FSMContext):
    """Редактирование информации: Какие платежи меня ожидают?"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.", parse_mode="HTML")
        await state.set_state(Formbag_tape.text_bag_tape)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.", parse_mode="HTML")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formbag_tape.text_bag_tape)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info,
                  file_path='messages/types_packaging_messages/bag_tape_messages.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.", parse_mode="HTML")
    await state.clear()


def bag_tape_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(bag_tape_handlers)  # Метод регистрации сообщений Мешок + скотч
    dp.message.register(bag_tape_handlers)  # Редактирование информации: Мешок + скотч
