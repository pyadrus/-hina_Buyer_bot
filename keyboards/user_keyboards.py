from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура главного меню"""
    rows = [
        [InlineKeyboardButton(text="⭐️ Услуги и цены", callback_data="services_and_prices")],
        [InlineKeyboardButton(text='🗒 Бланк заказа', callback_data="order_form")],
        [InlineKeyboardButton(text='🛍 Самовыкуп', callback_data="self_purchase")],
        [InlineKeyboardButton(text='📦 Виды упаковки', callback_data="types_packaging")],
        [InlineKeyboardButton(text='💌 Отзывы', callback_data="reviews")],
        [InlineKeyboardButton(text='📚 Полезная информация', callback_data="useful_information")],
        [InlineKeyboardButton(text='🔄 Обновить бота', callback_data="update_bot")],
        [InlineKeyboardButton(text='📞 Связаться с менеджером', callback_data="contact_manager")],
    ]

    main_menu_key = InlineKeyboardMarkup(inline_keyboard=rows)

    return main_menu_key


if __name__ == '__main__':
    main_menu_keyboard()
