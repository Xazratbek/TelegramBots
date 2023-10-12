from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ChatActions
from loader import dp
from keyboards.default.main_menu import main_menu
import time


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    time.sleep(1)
    await message.answer(f"Salom, {message.from_user.full_name}!\nMenga YouTubedan video linkini yuboring men uni sizga transcriptini yoki summarysini yuboraman",reply_markup=main_menu)
