import os

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


@router.message(Command("warranty_service_photo"))
async def warranty_service_photo(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, отправьте новое фото для замены в формате png", parse_mode="HTML")


@router.message(F.photo)
async def replace_photo(message: types.Message):
    # Получаем файл фотографии
    photo = message.photo[-1]
    file_info = await message.bot.get_file(photo.file_id)
    new_photo_path = os.path.join("messages/image/", '4.png')
    # Загружаем файл на диск
    await message.bot.download_file(file_info.file_path, new_photo_path)
    await message.answer("Фото успешно заменено!", parse_mode="HTML")


@router.callback_query(F.data == "warranty_service")
async def goods_redemption_service_handlers(callback_query: types.CallbackQuery):
    """Выкуп товаров"""
    logger.debug(callback_query)
    logger.debug(callback_query.message.message_id)
    main_menu_key = selection_goods_keyboard()

    data = load_bot_info_services_and_prices(file_path="messages/goods_redemption_service_messages.json")
    document = FSInputFile('messages/image/4.png')
    media = InputMediaPhoto(media=document, caption=data)

    await bot.edit_message_media(media=media,
                                 chat_id=callback_query.message.chat.id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=main_menu_key
                                 )


class FormWarrantyService(StatesGroup):
    text_warranty_service = State()


# Обработчик команды /edit_warranty_service (только для админа)
@router.message(Command("edit_warranty_service"))
async def edit_warranty_service(message: Message, state: FSMContext):
    """Редактирование информации: Выкуп товаров"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Введите новый текст, используя разметку HTML.", parse_mode="HTML")
        await state.set_state(FormWarrantyService.text_warranty_service)
    else:
        await message.reply("У вас нет прав на выполнение этой команды.", parse_mode="HTML")


# Обработчик текстовых сообщений (для админа, чтобы обновить информацию)
@router.message(FormWarrantyService.text_warranty_service)
async def update_info(message: Message, state: FSMContext):
    text = message.html_text
    bot_info = text
    save_bot_info(bot_info, file_path="messages/goods_redemption_service_messages.json")  # Сохраняем информацию в JSON
    await message.reply("Информация обновлена.", parse_mode="HTML")
    await state.clear()


def goods_redemption_service_handlers_register_message_handler():
    """Регистрируем handlers для бота"""
    dp.message.register(goods_redemption_service_handlers)  # Выкуп товаров
    dp.message.register(edit_warranty_service)  # Редактирование информации: Выкуп товаров
    dp.message.register(warranty_service_photo)  # Редактирование информации: Выкуп товаров
