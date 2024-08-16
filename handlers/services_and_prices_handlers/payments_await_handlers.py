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


@router.callback_query(F.data == "payment_options")
async def payments_await_handlers(callback_query: types.CallbackQuery):
    """Какие платежи меня ожидают?"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = selection_goods_keyboard()

    data = load_bot_info_services_and_prices(file_path='messages/payments_await_messages.json')

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_key, parse_mode="HTML"
    )


class Formpayment_options(StatesGroup):
    text_payment_options = State()


# Обработчик команды /edit_payment_options (только для админа)
@router.message(Command("edit_payment_options"))
async def edit_payment_options(message: Message, state: FSMContext):
    """Редактирование информации: Какие платежи меня ожидают?"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.", parse_mode="HTML")
        await state.set_state(Formpayment_options.text_payment_options)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.", parse_mode="HTML")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formpayment_options.text_payment_options)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='messages/payments_await_messages.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.", parse_mode="HTML")
    await state.clear()


def payments_await_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(payments_await_handlers)  # Какие платежи меня ожидают?
    dp.message.register(edit_payment_options)  # Редактирование: Какие платежи меня ожидают?
