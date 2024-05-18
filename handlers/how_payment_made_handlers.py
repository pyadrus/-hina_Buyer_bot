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


@router.callback_query(F.data == "payment_process")
async def how_payment_made_handlers(callback_query: types.CallbackQuery):
    """Как совершается оплата?"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = selection_goods_keyboard()

    data = load_bot_info_services_and_prices(file_path="messages/how_payment_made_messages.json")

    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=data,
        reply_markup=main_menu_key
    )


class FormPayment_process(StatesGroup):
    text_payment_process = State()


# Обработчик команды /edit_payment_process (только для админа)
@router.message(Command("edit_payment_process"))
async def edit_payment_process(message: Message, state: FSMContext):
    """Редактирование информации: Как совершается оплата?"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(FormPayment_process.text_payment_process)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormPayment_process.text_payment_process)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path="messages/how_payment_made_messages.json")  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def how_payment_made_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(how_payment_made_handlers)  # Как совершается оплата?
    dp.message.register(how_payment_made_handlers)  # Редактирование информации: Как совершается оплата?
