from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import types_packaging_keyboard
from services.services import load_bot_info_services_and_prices, save_bot_info
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "types_packaging_handlers")
async def types_packaging_handlers(callback_query: types.CallbackQuery):
    """Назад к видам упаковки"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = types_packaging_keyboard()

    data = load_bot_info_services_and_prices(
        file_path="messages/types_packaging_messages/types_packaging_massages.json")
    document = FSInputFile('messages/image/6.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


class Formtypes_packaging_handlers(StatesGroup):
    text_types_packaging_handlers = State()


# Обработчик команды /edit_types_packaging_handlers (только для админа)
@router.message(Command("edit_types_packaging_handlers"))
async def edit_types_packaging_handlers(message: Message, state: FSMContext):
    """Редактирование информации: Назад к видам упаковки"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Formtypes_packaging_handlers.text_types_packaging_handlers)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formtypes_packaging_handlers.text_types_packaging_handlers)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info,
                  file_path="messages/messages/types_packaging_messages/types_packaging_massages.json")  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def types_packaging_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(types_packaging_handlers)  # Регистрируем обработчик сообщений Назад к видам упаковки
    dp.message.register(edit_types_packaging_handlers)  # Редактирование информации: Назад к видам упаковки
