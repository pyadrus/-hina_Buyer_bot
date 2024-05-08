import asyncio
import logging
import sys

from handlers.delivery_goods_from_china_handlers import delivery_goods_from_china_handlers_register_message_handler
from handlers.main_menu_handlers import main_menu_register_message_handler
from handlers.selection_goods_analyst_sale_marketplaces_handlers import \
    selection_goods_analyst_sale_marketplaces_register_message_handler
from handlers.services_and_prices_handlers import services_and_prices_register_message_handler
from system.dispatcher import dp, bot


async def main() -> None:
    # bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)
    services_and_prices_register_message_handler()
    main_menu_register_message_handler()
    selection_goods_analyst_sale_marketplaces_register_message_handler()
    delivery_goods_from_china_handlers_register_message_handler()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
