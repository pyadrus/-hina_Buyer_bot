import json

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import services_and_prices_keyboard
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


def load_bot_info_services_and_prices():
    with open("messages/services_and_prices_messages.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.callback_query(F.data == "services_and_prices")
async def services_and_prices_handler(callback_query: types.CallbackQuery):
    """⭐️ Услуги и цены"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = services_and_prices_keyboard()

    data = load_bot_info_services_and_prices()
    document = FSInputFile('messages/image/1.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


class Formservices_and_prices(StatesGroup):
    textservices_and_prices = State()


# Сохранение информации в JSON-файл
def save_bot_info(data):
    with open("messages/services_and_prices_messages.json", 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# Обработчик команды /edit_services_and_prices (только для админа)
@router.message(Command("edit_services_and_prices"))
async def edit_services_and_prices(message: Message, state: FSMContext):
    """Редактирование информации: ⭐️ Услуги и цены"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Formservices_and_prices.textservices_and_prices)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formservices_and_prices.textservices_and_prices)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info)  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def services_and_prices_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(services_and_prices_handler)
    dp.message.register(edit_services_and_prices)
