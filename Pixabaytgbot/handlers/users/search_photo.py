import logging
import time
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.many_buttons import main_menu_btn
from aiogram.types import ReplyKeyboardRemove
from states.many_states import TextForSearchPhoto,Results
import requests
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import time
from keyboards.default.many_buttons import results


@dp.message_handler(text_contains="Rasm qidirish 🔎 🖼")
async def answer(message: Message):
    # await message.reply(f"Natijalar siz istagandek chiqishi uchun qidirish sozlamalarini sozlang 🛠⚙️")
    await message.answer("Rasm qidirish uchun Ingliz tilida biror so'z yuboring\n\nNamuna: <code>Tesla</code>",parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    await TextForSearchPhoto.text.set()

@dp.message_handler(text_contains="/start",state=TextForSearchPhoto.text)
async def answer(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu_btn)

@dp.message_handler(state=TextForSearchPhoto.text)
async def send_images(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {"text": text}
    )
    data = await state.get_data()
    text = data.get("text")
    url = f"https://pixabay.com/api/?key=22968062-150924647d813fab458caf2fb&q={text}&image_type=photo&pretty=true&safesearch=true"
    r = requests.get(url)
    res = r.json()
    await state.update_data(
        {"res": res}
    )

    if res['hits']:
        result = ""
        for i in range(len(res['hits'])):
            result += f"{i+1}). " + res['hits'][i]['tags'].title() + "\n"
        await message.answer(f"Ushbu Natijalardan birini pastdagi raqamlar orqali tanlang\n\n{result}",reply_markup=results)

        await Results.number.set()
    else:
        await message.answer("sizning so'rovingiz bo'yicha hech qanday natija mavjud emas")
        await TextForSearchPhoto.text.set()

@dp.message_handler(text_contains="❌" or "/start",state=Results.number)
async def answer(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu_btn)

@dp.message_handler(state=Results.number)
async def send_images(message: Message, state: FSMContext):
    number = message.text
    await state.update_data(
        {"number": number}
    )
    data = await state.get_data()
    text = data.get("text")
    number = data.get("number")
    res = data.get("res")
    number = int(number)

    await message.answer_photo(res['hits'][number-1]['largeImageURL'],caption=f"Tags 🇺🇸: {res['hits'][number-1]['tags'].title()}\nTeglar 🇺🇿: {res['hits'][number-1]['tags']}\nKo'rishlar soni: {res['hits'][number-1]['views']} 👀\nYuklanmalar soni: {res['hits'][number-1]['downloads']} ⬇️\nLikelar soni: {res['hits'][number-1]['likes']} 👍\nCommentlar soni: {res['hits'][number-1]['comments']} 💬\nTelegram bot: @pixabaytgbot 🤖\nTelegram kanal: @pixabaytgbot  📸🖼",reply_markup=results)
