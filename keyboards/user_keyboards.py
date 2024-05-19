from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


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
        [InlineKeyboardButton(text='📞 Связаться с менеджером', url='https://t.me/ChinaaBuyer')],
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


def create_my_details_keyboard():
    """Создает клавиатуру для кнопки 'Мои данные'"""
    my_details_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Регистрация', callback_data='my_details')]
    ])

    return my_details_keyboard


def create_data_modification_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру для изменения данных"""
    # data_modification_keyboard = InlineKeyboardMarkup()
    rows = [
        [InlineKeyboardButton(text="✏️Изменить Имя", callback_data="edit_name"),
         InlineKeyboardButton(text="✏️Изменить Фамилию", callback_data="edit_surname")],

        [InlineKeyboardButton(text="✏️Изменить Город", callback_data="edit_city"),
         InlineKeyboardButton(text="✏️Изменить Номер 📱 ", callback_data="edit_phone")],
        [InlineKeyboardButton(text="↩️ Вернуться в начальное меню", callback_data="disagree")]]

    data_modification_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return data_modification_keyboard


def create_sign_up_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру для кнопок 'Согласен' и 'Не согласен'"""
    # sign_up_keyboard = InlineKeyboardMarkup()
    rows = [
        [InlineKeyboardButton(text='👍 Согласен', callback_data='agree'),
         InlineKeyboardButton(text='👎 Не согласен', callback_data='disagree')]]

    sign_up_keyboard = InlineKeyboardMarkup(inline_keyboard=rows)
    return sign_up_keyboard


def create_contact_keyboard():
    """Создает клавиатуру для отправки контакта"""
    rows = [
        [KeyboardButton(text="📱 Отправить", request_contact=True)]
    ]

    contact_keyboard = ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True, one_time_keyboard=True)
    return contact_keyboard


if __name__ == '__main__':
    main_menu_keyboard()
