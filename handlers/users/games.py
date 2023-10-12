from aiogram.types import Message
import asyncio
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from keyboards.default.main_menu import main_menu, create_keyboard, create_inline_web_button, game_names
from states.buttons_state import TrackUser
import json
import re

def extract_numbers(text):
    # Matndan raqamlarni ajratish uchun regex
    numbers = re.findall(r'\d+', text)
    return [int(num) for num in numbers]  # Raqamlarni int ko'rinishida qaytaradi

@dp.message_handler(state=TrackUser.part,text_contains="Ortga 🔙")
async def send_inline_button(message: Message, state: FSMContext):
    await message.answer("Siz asosiy menyuga qaytdingiz")


@dp.message_handler(state=TrackUser.part)
async def send_inline_button(message: Message, state: FSMContext):
    try:
        nums = extract_numbers(message.text)
        await message.answer("Kerakli o'yin nomini tanlang",reply_markup=await create_keyboard(nums[0],nums[1]))
        await TrackUser.game_name.set()
    except IndexError:
        pass

@dp.message_handler(state=TrackUser.game_name,text_contains="Ortga 🔙")
async def send_inline_button(message: Message, state: FSMContext):
    nums = extract_numbers(message.text)
    await message.answer("Bizning botda 500-dan ortiq o'yinlar borligi sababli har bir 50-ta o'yin nomini alohida menyularga kirganganmiz.\n1. Biror bir menyuni kiriting\n2. Kerakli o'yinni nomiga qarab tanlang\n3 Miriqib o'yinni o'ynashingiz mumkin 😊\n@FunGameZonebot 🎮 😎",reply_markup=main_menu)
    await TrackUser.part.set()

@dp.message_handler(state=TrackUser.game_name)
async def send_inline_button(message: Message, state: FSMContext):

    if message.text in game_names:
        with open('games_data/games_name_data.json', 'r', encoding='utf-8') as file:
            games_data = json.load(file)


        await message.answer_photo(games_data[message.text]['Image Source'],message.text+"\n\n@FunGameZonebot 🎮 😎",reply_markup=await create_inline_web_button(message.text,"https://html5games.com"+games_data[message.text]['link']))
    else:
        await message.answer("Iltimos pastdagi o'yinlardan birini tanlang")
