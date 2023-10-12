from loader import dp
from aiogram.types import Message
from keyboards.inline.any_inline_btns import share

@dp.message_handler(text_contains="Botni ulashish 🚀")
async def answer(message: Message):
    await message.answer("<b>Ulashmoqchi bo'lgan chatingizni tanlang\n\n@islom_dini_uchun_bot</b>",reply_markup=share,parse_mode="HTML")