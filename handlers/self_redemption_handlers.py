from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import main_menu_selection_keyboard
from services.services import load_bot_info_services_and_prices, save_bot_info
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "self_purchase")
async def self_redemption_handlers(callback_query: types.CallbackQuery):
    """🛍 Самовыкуп"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = main_menu_selection_keyboard()

    data = load_bot_info_services_and_prices(file_path="messages/self_redemption_messages.json")
    document = FSInputFile('messages/image/5.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


class Formservices_self_purchase(StatesGroup):
    textself_purchase = State()


# Обработчик команды /edit_self_purchase (только для админа)
@router.message(Command("edit_self_purchase"))
async def edit_self_purchase(message: Message, state: FSMContext):
    """Редактирование информации: 🛍 Самовыкуп"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Formservices_self_purchase.textself_purchase)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formservices_self_purchase.textself_purchase)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path="messages/self_redemption_messages.json")  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def self_redemption_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(self_redemption_handlers)
    dp.message.register(edit_self_purchase)
