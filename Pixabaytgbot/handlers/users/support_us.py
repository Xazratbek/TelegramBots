from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.many_buttons import main_menu_btn,tolov_tizimlari
from states.many_states import Payments


@dp.message_handler(state=Payments.payments,text_contains="Ortga 🔙")
async def answer(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu_btn)

@dp.message_handler(text_contains="Loyihani qo'llab quvvatlash 💳 💲",state=None)
async def answer(message: Message):
    await message.answer("Qaysi To'lov tizimidan foydalanib Loyihani qo'llab quvvatlamoqchisiz",reply_markup=ReplyKeyboardRemove())
    await message.answer("Tanlang 👇",reply_markup=tolov_tizimlari)
    await Payments.payments.set()

@dp.message_handler(text_contains="CLICK ilovasi 💠",state=Payments.payments)
async def answer(message: Message):
    await message.answer("<b>Karta raqam: <code>9860 0301 7268 0750 </code>\nKarta egasi: Turdaliyev Xazratbek Nozimjon og'li \nTelegram aloqa: @xazratbek27\n\n@pixabaytgbot 🔎 🖼</b>",parse_mode="HTML")

@dp.message_handler(text_contains="Payme ilovasi 📱",state=Payments.payments)
async def answer(message: Message):
    await message.answer("<b>Payme ilovasidan karta raqamiga pul o'tkazishingiz mumkin:\nhttps://payme.uz/@xazratbek_ \nKarta raqam: <code>9860 0301 7268 0750 </code>\nKarta egasi: Turdaliyev Xazratbek Nozimjon og'li\nTelegram aloqa: @xazratbek27 \n\n@pixabaytgbot 🔎 🖼</b>",parse_mode="HTML",disable_web_page_preview=True)

@dp.message_handler(text_contains="Apelsin ilovasi 🍊",state=Payments.payments)
async def answer(message: Message):
    await message.answer("<b>Karta raqam: <code>9860 0301 7268 0750 </code>\nKarta egasi: Turdaliyev Xazratbek Nozimjon og'li \nTelegram aloqa: @xazratbek27\n\n@pixabaytgbot 🔎 🖼</b>",parse_mode="HTML")

@dp.message_handler(text_contains="Karta raqam orqali 💳",state=Payments.payments)
async def answer(message: Message):
    await message.answer("<b><code>Karta raqam: 9860 0301 7268 0750 </code>\nKarta egasi: Turdaliyev Xazratbek Nozimjon og'li \nTelegram aloqa: @xazratbek27 \n\n@pixabaytgbot 🔎 🖼</b>",parse_mode="HTML")