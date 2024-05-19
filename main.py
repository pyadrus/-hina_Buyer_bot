import asyncio
import logging
import sys

from handlers.main_menu_handlers import main_menu_register_message_handler
from handlers.order_form_handlers import order_form_handlers_handlers_register_message_handler
from handlers.reviews_handlers.reviews_handlers import reviews_handlers_register_message_handler
from handlers.self_redemption_handlers import self_redemption_handlers_register_message_handler
from handlers.services_and_prices_handlers.delivery_goods_from_china_handlers import \
    register_delivery_goods_from_china_handlers
from handlers.services_and_prices_handlers.goods_redemption_service_handlers import \
    goods_redemption_service_handlers_register_message_handler
from handlers.services_and_prices_handlers.how_payment_made_handlers import \
    how_payment_made_handlers_register_message_handler
from handlers.services_and_prices_handlers.payments_await_handlers import \
    payments_await_handlers_register_message_handler
from handlers.services_and_prices_handlers.product_search_service_handlers import \
    product_search_service_handlers_register_message_handler
from handlers.services_and_prices_handlers.selection_goods_analyst_sale_marketplaces_handlers import \
    register_product_search_handlers
from handlers.services_and_prices_handlers.services_and_prices_handlers import \
    services_and_prices_register_message_handler
from handlers.types_packaging_handlers.bag_tape_handlers import bag_tape_handlers_register_message_handler
from handlers.types_packaging_handlers.box_bag_tape_handlers import box_bag_tape_handlers_register_message_handler
from handlers.types_packaging_handlers.cardboard_corners_bag_tape_handlers import \
    cardboard_corners_bag_tape_handlers_register_message_handler
from handlers.types_packaging_handlers.pallet_crate_handlers import pallet_crate_handlers_register_message_handler
from handlers.types_packaging_handlers.pallet_with_solid_wooden_box_handlers import \
    pallet_with_solid_wooden_box_handlers_register_message_handler
from handlers.types_packaging_handlers.types_packaging_handlers import types_packaging_handlers_register_message_handler
from handlers.types_packaging_handlers.wooden_sheathing_bag_tape_handlers import \
    wooden_sheathing_bag_tape_handlers_register_message_handler
from system.dispatcher import dp, bot


async def main() -> None:
    await dp.start_polling(bot)
    services_and_prices_register_message_handler()
    main_menu_register_message_handler()
    register_product_search_handlers()
    register_delivery_goods_from_china_handlers()
    goods_redemption_service_handlers_register_message_handler()
    product_search_service_handlers_register_message_handler()
    how_payment_made_handlers_register_message_handler()
    order_form_handlers_handlers_register_message_handler()
    payments_await_handlers_register_message_handler()
    self_redemption_handlers_register_message_handler()
    types_packaging_handlers_register_message_handler()
    bag_tape_handlers_register_message_handler()
    box_bag_tape_handlers_register_message_handler()
    wooden_sheathing_bag_tape_handlers_register_message_handler()
    cardboard_corners_bag_tape_handlers_register_message_handler()
    pallet_crate_handlers_register_message_handler()
    pallet_with_solid_wooden_box_handlers_register_message_handler()
    reviews_handlers_register_message_handler()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
