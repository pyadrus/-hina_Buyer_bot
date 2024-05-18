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
                             "/edit_services_and_prices - редактирование: ⭐️ Услуги и цены\n"
                             "/edit - редактирование: пост приветствиt\n"
                             "/edit_self_purchase - редактирование: 🛍 Самовыкуп\n"
                             "/edit_product_search - редактирование: Подбор товара\n"
                             "/edit_search_in_china - редактирование: Поиск поставщика в Китае\n"
                             "/edit_warranty_service - редактирование: Выкуп товаров\n"
                             "/edit_delivery_in_china - редактирование: Доставка в Китае\n"
                             "/edit_payment_process - редактирование: Как совершается оплата?\n"
                             "/edit_order_form - редактирование: 🗒 Бланк заказа\n"
                             "/edit_payment_options - редактирование: Какие платежи меня ожидают?\n"
                             "/edit_reviews - редактирование: 💌 Отзывы\n"
                             "/edit_bag_tape - редактирование: Мешок + скотч\n"
                             "/edit_box_bag_tape - редактирование: Коробка + мешок + скотч\n"
                             "/edit_cardboard_corners_bag_tape - редактирование: Картонные уголки + мешок + скотч\n"
                             "/edit_pallet_crate - редактирование: Паллет в обрешетке\n"
                             "edit_pallet_with_solid_wooden_box - редактирование: Паллет с глухим деревянным коробом\n"
                             "/edit_types_packaging_handlers - редактирование: Назад к видам упаковки\n"
                             "/edit_wooden_sheathing_bag_tape - редактирование: Деревянная обрешетка + мешок + скотч\n\n"
                             "/start - начальное меню\n")
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


def register_handlers_admin():
    dp.message.register(help_handler)
