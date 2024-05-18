from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message
from loguru import logger

from keyboards.user_keyboards import main_menu_selection_keyboard
from services.services import save_bot_info, load_bot_info_services_and_prices
from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import bot
from system.dispatcher import dp
from system.dispatcher import router


@router.callback_query(F.data == "reviews")
async def reviews_handlers(callback_query: types.CallbackQuery):
    """💌 Отзывы"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = main_menu_selection_keyboard()

    data = load_bot_info_services_and_prices(file_path="messages/reviews_messages/reviews_messages.json")
    document = FSInputFile('messages/image/1.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


class Formreviews(StatesGroup):
    text_reviews = State()


# Обработчик команды /edit_reviews (только для админа)
@router.message(Command("edit_reviews"))
async def edit_reviews(message: Message, state: FSMContext):
    """Редактирование информации: 💌 Отзывы"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.")
        await state.set_state(Formreviews.text_reviews)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(Formreviews.text_reviews)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path='messages/reviews_messages/reviews_messages.json')  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.")
    await state.clear()


def reviews_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(reviews_handlers)  # Регистрируем обработчик 💌 Отзывы
    dp.message.register(edit_reviews)  # Редактирование информации: 💌 Отзывы
