from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncpg
from loader import dp, db

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    import requests
    from io import BytesIO


    try:
        user = await db.add_user(message.from_user.first_name,message.from_user.last_name,message.from_user.username,message.from_user.id,is_active=1)
        await message.answer(f"Salom {message.from_user.first_name} 👋\nBotimizga Xush kelibsiz!\nBot imkoniyatlari haqida ma'lumot olish uchun /info buyrug'ini yuboring")
    except asyncpg.exceptions.UniqueViolationError:
        await db.set_active(message.from_user.id, 1)
        await message.answer(f"Salom {message.from_user.first_name} 👋\nBotimizga Xush kelibsiz!\nBot imkoniyatlari haqida ma'lumot olish uchun /info buyrug'ini yuboring")