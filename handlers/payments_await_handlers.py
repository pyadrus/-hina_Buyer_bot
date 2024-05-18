from aiogram import types, F
from loguru import logger

from keyboards.user_keyboards import selection_goods_keyboard
from services.services import load_bot_info_services_and_prices
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "payment_options")
async def payments_await_handlers(callback_query: types.CallbackQuery):
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = selection_goods_keyboard()

    data = load_bot_info_services_and_prices(file_path='messages/payments_await_messages.json')

    await bot.edit_message_caption(
                                   chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption=data,
                                   reply_markup=main_menu_key
                                   )


def payments_await_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(payments_await_handlers)
