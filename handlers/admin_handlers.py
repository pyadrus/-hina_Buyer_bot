from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from system.dispatcher import ADMIN_USER_ID
from system.dispatcher import dp
from system.dispatcher import router


@router.message(Command("help"))
async def help_handler(message: Message, state: FSMContext):
    """Админ панель"""
    if message.from_user.id == ADMIN_USER_ID:
        await message.answer("Команды админа:\n\n"
                             "/edit_services_and_prices - редактирование ⭐️ Услуги и цены\n"
                             "/edit - редактирование поста приветствия\n"
                             "/edit_self_purchase - редактирование 🛍 Самовыкуп\n"
                             "/edit_product_search - редактирование Подбор товара\n"
                             "/edit_search_in_china - редактирование Поиск поставщика в Китае\n"
                             
                             "/edit_warranty_service - редактирование Выкуп товаров\n"
                             "/edit_delivery_in_china - редактирование Доставка в Китае\n"
                             "/edit_payment_process - редактирование Как совершается оплата?\n"
                             "/edit_order_form - редактирование 🗒 Бланк заказа"
                             "/start - начальное меню\n")
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


def register_handlers_admin():
    dp.message.register(help_handler)
