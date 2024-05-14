import json

from aiogram import types, F
from aiogram.types import FSInputFile, InputMediaPhoto
from loguru import logger

from keyboards.user_keyboards import types_packaging_keyboard
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


def load_bot_info_services_and_prices():
    with open("messages/types_packaging_messages/types_packaging_massages.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "types_packaging_handlers")
async def types_packaging_handlers(callback_query: types.CallbackQuery):
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = types_packaging_keyboard()

    data = load_bot_info_services_and_prices()
    document = FSInputFile('messages/image/6.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


def types_packaging_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(types_packaging_handlers)
