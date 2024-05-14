from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура главного меню"""
    rows = [
        [InlineKeyboardButton(text="⭐️ Услуги и цены", callback_data="services_and_prices"),
         InlineKeyboardButton(text='🗒 Бланк заказа', callback_data="order_form")],
        [InlineKeyboardButton(text='🛍 Самовыкуп', callback_data="self_purchase")],
        [
            InlineKeyboardButton(text='📦 Виды упаковки', callback_data="types_packaging_handlers"),
            InlineKeyboardButton(text='💌 Отзывы', callback_data="reviews"),
        ],
        [InlineKeyboardButton(text='📚 Полезная информация', callback_data="useful_information")],
        # [InlineKeyboardButton(text='🔄 Обновить бота', callback_data="update_bot")],
        [InlineKeyboardButton(text='📞 Связаться с менеджером', callback_data="contact_manager")],
    ]

    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)

    return main_menu_key


def services_and_prices_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с услугами и ценами"""
    rows = [
        [InlineKeyboardButton(text="Подбор товара", callback_data="product_search"),
         InlineKeyboardButton(text="Выкуп товаров", callback_data="warranty_service")],
        [InlineKeyboardButton(text="Поиск поставщика в Китае", callback_data="search_in_china")],
        [InlineKeyboardButton(text="Доставка товаров из Китая", callback_data="delivery_in_china")],
        [InlineKeyboardButton(text="Какие платежи меня ожидают?", callback_data="payment_options")],
        [InlineKeyboardButton(text="Как совершается оплата?", callback_data="payment_process")],
        [InlineKeyboardButton(text="↩️Главное меню", callback_data="main_menu")],
    ]
    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_menu_key


def main_menu_selection_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text="↩️Главное меню", callback_data="main_menu")],
    ]
    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_menu_key


def selection_goods_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура выбора товара"""
    rows = [
        [InlineKeyboardButton(text='Назад к услугам', callback_data="services_and_prices")],
        [InlineKeyboardButton(text='↩️Главное меню', callback_data="main_menu")],
    ]
    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_menu_key


def types_packaging_keyboard() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text="Мешок + скотч", callback_data="bag_tape")],
        [InlineKeyboardButton(text="Коробка + мешок + скотч", callback_data="box_bag_tape")],
        [InlineKeyboardButton(text="Деревянная обрешетка + мешок + скотч", callback_data="wooden_sheathing_bag_tape")],
        [InlineKeyboardButton(text="Картонные уголки + мешок + скотч", callback_data="cardboard_corners_bag_tape")],
        [InlineKeyboardButton(text="Паллет в обрешетке", callback_data="pallet_crate")],
        [InlineKeyboardButton(text="Паллет с глухим деревянным коробом", callback_data="pallet_with_solid_wooden_box")],
        [InlineKeyboardButton(text="↩️Главное меню", callback_data="main_menu")],
    ]
    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_menu_key


def tapes_packing_keyboard_back() -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text='Назад к видам упаковки', callback_data="types_packaging_handlers")],
        [InlineKeyboardButton(text='↩️Главное меню', callback_data="main_menu")],
    ]
    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)
    return main_menu_key


if __name__ == '__main__':
    main_menu_keyboard()
