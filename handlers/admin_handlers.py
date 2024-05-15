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
                             "/edit_self_purchase - редактирование 🛍 Самовыкуп")
    else:
        await message.reply("У вас нет прав на выполнение этой команды.")


def register_handlers_admin():
    dp.message.register(help_handler)
