import json

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import main_menu_selection_keyboard
from services.services import load_bot_info_services_and_prices, save_bot_info
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "order_form")
async def order_form_handlers_handlers(callback_query: types.CallbackQuery):
    """🗒 Бланк заказа"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = main_menu_selection_keyboard()

    data = load_bot_info_services_and_prices(file_path="messages/order_form_handlers_messages.json")

    document = FSInputFile('messages/Бланк_заказа_ChinaBuyer.xlsx')
    await bot.send_document(chat_id=callback_query.message.chat.id, document=document, reply_markup=main_menu_key,
                            caption=data)


class Formedit_order_form(StatesGroup):
    text_edit_order_form = State()


# Обработчик команды /edit_order_form (только для админа)
@router.message(Command("edit_order_form"))
async def edit_order_form(message: Message, state: FSMContext):
    """Редактирование информации: 🗒 Бланк заказа"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Formedit_order_form.text_edit_order_form)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formedit_order_form.text_edit_order_form)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path="messages/order_form_handlers_messages.json")  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def order_form_handlers_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(order_form_handlers_handlers)  # 🗒 Бланк заказа
    dp.message.register(edit_order_form)  # Редактирование информации: 🗒 Бланк заказа
