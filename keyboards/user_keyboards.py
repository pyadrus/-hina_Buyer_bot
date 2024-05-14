from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура главного меню"""
    rows = [
        [InlineKeyboardButton(text="⭐️ Услуги и цены", callback_data="services_and_prices")],
        [InlineKeyboardButton(text='🗒 Бланк заказа', callback_data="order_form")],
        [InlineKeyboardButton(text='🛍 Самовыкуп', callback_data="self_purchase")],
        [
            InlineKeyboardButton(text='📦 Виды упаковки', callback_data="types_packaging"),
            InlineKeyboardButton(text='💌 Отзывы', callback_data="reviews"),
        ],
        [InlineKeyboardButton(text='📚 Полезная информация', callback_data="useful_information")],
        [InlineKeyboardButton(text='🔄 Обновить бота', callback_data="update_bot")],
        [InlineKeyboardButton(text='📞 Связаться с менеджером', callback_data="contact_manager")],
    ]

    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)

    return main_menu_key


def services_and_prices_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с услугами и ценами"""
    rows = [
        [InlineKeyboardButton(text="Услуга подбора товара аналитиком для продажи на МП",
                              callback_data="product_search")],
        [InlineKeyboardButton(text="Услуга Выкупа товаров", callback_data="warranty_service")],
        [InlineKeyboardButton(text="Услуга Поиска товаров (производителей в Китае)", callback_data="search_in_china")],
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


if __name__ == '__main__':
    main_menu_keyboard()
