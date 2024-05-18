import json

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import selection_goods_keyboard
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


def load_bot_info_services_and_prices():
    with open("messages/delivery_goods_from_china_messages.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "delivery_in_china")
async def delivery_goods_from_china_handlers(callback_query: types.CallbackQuery):
    """Доставка товаров из Китая"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = selection_goods_keyboard()

    data = load_bot_info_services_and_prices()
    document = FSInputFile('messages/image/3.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )

class FormDeliveryInChina(StatesGroup):
    text_delivery_in_china = State()


# Сохранение информации в JSON-файл
def save_bot_info(data):
    with open("messages/delivery_goods_from_china_messages.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# Обработчик команды /edit_delivery_in_china (только для админа)
@router.message(Command("edit_delivery_in_china"))
async def edit_delivery_in_china(message: Message, state: FSMContext):
    """Редактирование информации: Доставка товаров из Китая"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(FormDeliveryInChina.text_delivery_in_china)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormDeliveryInChina.text_delivery_in_china)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info)  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def delivery_goods_from_china_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(delivery_goods_from_china_handlers)  # Доставка товаров из Китая
    dp.message.register(edit_delivery_in_china)  # Редактирование информации: Доставка товаров из Китая
