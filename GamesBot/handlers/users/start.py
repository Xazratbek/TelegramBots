from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_menu import main_menu
from loader import dp
from states.buttons_state import TrackUser

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await TrackUser.part.set()

    await message.answer("Bizning botda 500-dan ortiq o'yinlar borligi sababli har bir 50-ta o'yin nomini alohida menyularga kirganganmiz.\n1. Biror bir menyuni kiriting\n2. Kerakli o'yinni nomiga qarab tanlang\n3 Miriqib o'yinni o'ynashingiz mumkin 😊\n@FunGameZonebot 🎮 😎",reply_markup=main_menu)
