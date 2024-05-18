from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import selection_goods_keyboard
from services.services import load_bot_info_services_and_prices, save_bot_info
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "product_search")
async def handle_product_search(callback_query: types.CallbackQuery):
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = selection_goods_keyboard()

    data = load_bot_info_services_and_prices(file_path="messages/selection_goods_analyst_sale_marketplaces_messages.json")
    document = FSInputFile('messages/image/2.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


class ProductSearchForm(StatesGroup):
    product_search_text = State()


# Обработчик команды /edit_product_search (только для админа)
@router.message(Command("edit_product_search"))
async def handle_edit_product_search_command(message: Message, state: FSMContext):
    """Редактирование информации: Подбор товара"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(ProductSearchForm.product_search_text)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(ProductSearchForm.product_search_text)
async def handle_update_product_search_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path="messages/selection_goods_analyst_sale_marketplaces_messages.json")  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def register_product_search_handlers():
    """Регистрируем handlers для бота"""
    dp.message.register(handle_product_search)
    dp.message.register(handle_edit_product_search_command)
    dp.message.register(handle_update_product_search_info)
