import logging
import time
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.many_buttons import main_menu_btn
from aiogram.types import ReplyKeyboardRemove
from states.many_states import Results_for_video,TextForSearchVideo
import requests
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import time
from keyboards.default.many_buttons import results

from googletrans import Translator

translator = Translator()


@dp.message_handler(text_contains="Video qidirish 🔎 🎦")
async def answer(message: Message):
    # await message.reply(f"Natijalar siz istagandek chiqishi uchun qidirish sozlamalarini sozlang 🛠⚙️")
    await message.answer("Video qidirish uchun Ingliz tilida biror matn yuboring\n\nNamuna: <code>Pacific Ocean</code>",parse_mode="HTML",reply_markup=ReplyKeyboardRemove())
    await TextForSearchVideo.video.set()

@dp.message_handler(state=TextForSearchVideo.video)
async def send_images(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(
        {"text": text}
    )
    data = await state.get_data()
    text = data.get("text")
    url = f"https://pixabay.com/api/videos/?key=22968062-150924647d813fab458caf2fb&q={text.lower()}"
    r = requests.get(url)
    res = r.json()
    await state.update_data(
        {"res": res}
    )

    if res['hits']:
        result = ""
        for i in range(len(res['hits'])):
            result += f"{i+1}) " + res['hits'][i]['tags'].title() + "\n"
        await message.answer(f"Ushbu Natijalardan birini pastdagi raqamlar orqali tanlang\n\n{result}",reply_markup=results)

        await Results_for_video.number.set()


@dp.message_handler(text_contains="❌" or "/start",state=Results_for_video.number)
async def answer(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu_btn)

@dp.message_handler(state=Results_for_video.number)
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

    await message.answer_video(res['hits'][number-1]['videos']['medium']['url'],caption=f"Tags 🇺🇸: {res['hits'][number-1]['tags'].title()}\nTeglar 🇺🇿: {translator.translate(text=res['hits'][number-1]['tags'],dest='uz').text.title()}\nKo'rishlar soni: {res['hits'][number-1]['views']} 👀\nYuklanmalar soni: {res['hits'][number-1]['downloads']} ⬇️\nLikelar soni: {res['hits'][number-1]['likes']} 👍\nCommentlar soni: {res['hits'][number-1]['comments']} 💬\nTelegram bot: @pixabaytgbot 🤖\nTelegram kanal: @pixabaytgbot  📸🖼",disable_notification=True)