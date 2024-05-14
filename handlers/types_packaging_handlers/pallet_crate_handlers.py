import json

from aiogram import types, F
from loguru import logger

from keyboards.user_keyboards import tapes_packing_keyboard_back
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


def load_bot_info_services_and_prices():
    with open("messages/types_packaging_messages/pallet_crate_messages.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "pallet_crate")
async def pallet_crate_handlers(callback_query: types.CallbackQuery):
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    data = load_bot_info_services_and_prices()
    main_menu_key = tapes_packing_keyboard_back()
    # document = FSInputFile('messages/image/4.png')
    # media = InputMediaPhoto(caption=data)

    await bot.edit_message_caption(
                                   chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption=data,
                                   reply_markup=main_menu_key
                                   )


def pallet_crate_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(pallet_crate_handlers)
