from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni qayta ishga tushirish ♻️",
            "/help - Yordam olish 🆘 ",
            "/info - Bot imkoniyatlari haqida ma'lumot ℹ️\n\n@pixabaytgbot 🔎 🖼")

    await message.answer("\n".join(text))
