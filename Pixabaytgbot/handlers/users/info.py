from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command('info'))
async def bot_help(message: types.Message):
    await message.answer("<b>Siz ushbu bot orqali yuqori sifatdagi rasm va videolarni qdirib topishingiz mumkin.\n\n@pixabaytgbot 🔎 🖼</b>",parse_mode="HTML")
