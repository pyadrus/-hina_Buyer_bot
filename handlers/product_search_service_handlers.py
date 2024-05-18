from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import selection_goods_keyboard
from services.services import load_bot_info_services_and_prices, save_bot_info
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "search_in_china")
async def product_search_service_handlers(callback_query: types.CallbackQuery):
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = selection_goods_keyboard()

    data = load_bot_info_services_and_prices(file_path="messages/product_search_service_messages.json")

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_key
    )


class Formservices_search_in_china(StatesGroup):
    text_search_in_china = State()


# Обработчик команды /edit_product_search_service (только для админа)
@router.message(Command("edit_search_in_china"))
async def edit_search_in_china(message: Message, state: FSMContext):
    """Редактирование информации: Подбор товара"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Formservices_search_in_china.text_search_in_china)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formservices_search_in_china.text_search_in_china)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path="messages/product_search_service_messages.json")  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def product_search_service_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(product_search_service_handlers)
    dp.message.register(edit_search_in_china)
