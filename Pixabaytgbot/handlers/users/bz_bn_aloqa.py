import logging
import time
from aiogram.types import Message, CallbackQuery, ContentTypes
from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.many_buttons import cancel_btn,main_menu_btn
from keyboards.inline.any_inline_btns import aloqa_btn_inline,keyboard_for_aloqa
from states.many_states import Aloqa,Xatolik_topdim,Taklif_bor,Bz_bn_aloqa


@dp.message_handler(text_contains="Bekor qilish ❌",state=Taklif_bor.taklif)
async def answer(message: Message, state: FSMContext):
    await state.finish()
    await dp.bot.delete_message(message.chat.id,message_id=message.message_id)
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)

@dp.message_handler(text_contains="Bekor qilish ❌",state=Xatolik_topdim.xatolik)
async def answer(message: Message, state: FSMContext):
    await state.finish()
    await dp.bot.delete_message(message.chat.id,message_id=message.message_id)
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)

@dp.message_handler(text_contains="Biz bilan aloqa 💌")
async def answer(message: Message):
    await Aloqa.aloqa.set()
    await message.answer("Bot bo'yicha muroojat va takliflaringiz bo'lsa telegram kontakt: @xazratbek",reply_markup=ReplyKeyboardRemove())
    await message.answer("Nima haqida yozmoqchisiz ?",reply_markup=aloqa_btn_inline,parse_mode="HTML")

@dp.callback_query_handler(text_contains="taklif_bor",state=Aloqa.aloqa)
async def answer(call: CallbackQuery):
    await Taklif_bor.taklif.set()
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("<b>Eslatma ❗️ Siz yuborgan xabar, video xabar, ovozli xabar 3-shaxsga ko'rsatilmaydi va yuborilmaydi, sizdan kelayotgan fikr va mulohazalar faqatgina adminga ko'rinadi</b>\n\nO'z istak yoki takliflaringiz haqida batafsil yozib yuboring yoki ovozli xabar va videoxabar ko'rinishda yuboring 👇",reply_markup=bekor_qilish,parse_mode="HTML")

@dp.callback_query_handler(text_contains="xatolik_topdim",state=Aloqa.aloqa)
async def answer(call: CallbackQuery):
    await Xatolik_topdim.xatolik.set()
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("<b>Eslatma ❗️ Siz yuborgan xabar, video xabar, ovozli xabar 3-shaxsga ko'rsatilmaydi va yuborilmaydi, sizdan kelayotgan fikr va mulohazalar faqatgina adminga ko'rinadi</b>\n\nXatolik haqida batafsil yozib yuboring yoki ovozli xabar, videoxabar ko'rinishda yuboring 👇",reply_markup=bekor_qilish,parse_mode="HTML")

@dp.callback_query_handler(text_contains="cancel",state=Aloqa.aloqa)
async def answer(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.answer(cache_time=60)
    await state.finish()
    await call.message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)

###

@dp.message_handler(state=Taklif_bor.taklif)
async def answer(message: Message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.username
    await state.update_data(
        {"text": text}
    )
    data = await state.get_data()
    text = data.get("text")
    await dp.bot.send_message(1088163005,f"Foydalanuvchi ismi: {user_full_name}\n\nFoydalanuvchi telegram akkaunti uchun link: @{user_name}\n\nFoydalanuvchi id-raqami: <code>{user_id}</code>\n\nFoydalanuvchidan kelgan xabar: <code>{text}</code>\n\nXabar id-raqami: <code>{message.message_id}</code>",reply_markup=keyboard_for_aloqa,parse_mode="HTML")
    await state.finish()
    await message.reply("Xabaringiz yuborildi, tez orada adminlarimiz javob yozishadi fikr va mulohazalaringiz uchun rahmat! 😊\n\n@elektronformularbot 📝")
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)

@dp.message_handler(state=Xatolik_topdim.xatolik)
async def answer(message: Message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.username
    await state.update_data(
        {"text": text}
    )
    data = await state.get_data()
    text = data.get("text")
    await dp.bot.send_message(1088163005,f"Foydalanuvchi ismi: {user_full_name}\n\nFoydalanuvchi telegram akkaunti uchun link: @{user_name}\n\nFoydalanuvchi id-raqami: <code>{user_id}</code>\n\nFoydalanuvchidan kelgan xabar: <code>{text}</code>\n\nXabar id-raqami: <code>{message.message_id}</code>",parse_mode="HTML",reply_markup=keyboard_for_aloqa)
    await state.finish()
    await message.reply("Xabaringiz yuborildi, tez orada adminlarimiz javob yozishadi fikr va mulohazalaringiz uchun rahmat! 😊\n\n@elektronformularbot 📝")
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)


###

@dp.message_handler(state=Xatolik_topdim.xatolik,content_types=ContentTypes.VOICE)
async def answer(message: Message,state: FSMContext):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.username
    voice_ID = message.voice.file_id
    await dp.bot.send_voice(1088163005,voice=voice_ID,caption=f"Foydalanuvchi ismi: {user_full_name}\n\nFoydalanuvchi telegram akkaunti uchun link: @{user_name}\n\nFoydalanuvchi id-raqami: <code>{user_id}</code>\n\nXabar id-raqami: <code>{message.message_id}</code>",reply_markup=keyboard_for_aloqa,parse_mode="HTML")
    await state.finish()
    await message.reply("Ovozli xabar yuborildi, tez orada adminlarimiz javob yozishadi fikr va mulohazalaringiz uchun rahmat! 😊\n\n@elektronformularbot 📝")
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)

@dp.message_handler(state=Taklif_bor.taklif,content_types=ContentTypes.VOICE)
async def answer(message: Message,state: FSMContext):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.username
    voice_ID = message.voice.file_id
    await dp.bot.send_voice(1088163005,voice=voice_ID,caption=f"Foydalanuvchi ismi: {user_full_name}\n\nFoydalanuvchi telegram akkaunti uchun link: @{user_name}\n\nFoydalanuvchi id-raqami: <code>{user_id}</code>\n\nXabar id-raqami: <code>{message.message_id}</code>",reply_markup=keyboard_for_aloqa,parse_mode="HTML")
    await state.finish()
    await message.reply("Ovozli xabar yuborildi, tez orada adminlarimiz javob yozishadi fikr va mulohazalaringiz uchun rahmat! 😊\n\n@elektronformularbot 📝")
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)

@dp.message_handler(state=Xatolik_topdim.xatolik,content_types=ContentTypes.VIDEO_NOTE)
async def answer(message: Message,state: FSMContext):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.username
    videonote_ID = message.video_note.file_id
    await dp.bot.send_video_note(1088163005,video_note=videonote_ID)
    await dp.bot.send_message(1088163005,f"Foydalanuvchi ismi: {user_full_name}\n\nFoydalanuvchi telegram akkaunti uchun link: @{user_name}\n\nFoydalanuvchi id-raqami: <code>{user_id}</code>\n\nXabar id-raqami: <code>{message.message_id}</code>",reply_markup=keyboard_for_aloqa,parse_mode="HTML")
    await state.finish()
    await message.reply("Video xabar yuborildi, tez orada adminlarimiz javob yozishadi fikr va mulohazalaringiz uchun rahmat! 😊\n\n@elektronformularbot 📝")
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)

@dp.message_handler(state=Taklif_bor.taklif,content_types=ContentTypes.VIDEO_NOTE)
async def answer(message: Message,state: FSMContext):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.username
    videonote_ID = message.video_note.file_id
    await dp.bot.send_video_note(1088163005,video_note=videonote_ID)
    await dp.bot.send_message(1088163005,f"Foydalanuvchi ismi: {user_full_name}\n\nFoydalanuvchi telegram akkaunti uchun link: @{user_name}\n\nFoydalanuvchi id-raqami: <code>{user_id}</code>\n\nXabar id-raqami: <code>{message.message_id}</code>",reply_markup=keyboard_for_aloqa,parse_mode="HTML")
    await state.finish()
    await message.reply("Video xabar yuborildi, tez orada adminlarimiz javob yozishadi fikr va mulohazalaringiz uchun rahmat! 😊\n\n@elektronformularbot 📝")
    await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)


@dp.callback_query_handler(text_contains="answer_call")
async def answer(call: CallbackQuery):
    callback_data = call.data
    await call.answer(cache_time=60)
    await call.message.answer("Foydalanuvchining id-raqamini yuboring")
    await Bz_bn_aloqa.user_id.set()

@dp.message_handler(state=Bz_bn_aloqa.user_id)
async def answer(message: Message,state: FSMContext):
    user_id = message.text
    await state.update_data(
        {"user_id": user_id}
    )
    await message.answer("Foydalanuvchiga yubormoqchi bo'lgan xabaringizni yoki ovozli xabaringizni yuboring")
    await Bz_bn_aloqa.msg.set()

@dp.message_handler(state=Bz_bn_aloqa.msg,content_types=ContentTypes.VOICE)
async def answer(message: Message,state: FSMContext):
    msg_for_send_user = message.voice.file_id
    await state.update_data(
        {"msg_for_send_user": msg_for_send_user}
    )
    await message.answer("Xabar id-raqamini kiriting")
    await Bz_bn_aloqa.reply_to_message_id.set()

@dp.message_handler(state=Bz_bn_aloqa.msg)
async def answer(message: Message,state: FSMContext):
    msg_for_send_user = message.text
    await state.update_data(
        {"msg_for_send_user": msg_for_send_user}
    )
    await message.answer("Xabar id-raqamini kiriting")
    await Bz_bn_aloqa.reply_to_message_id.set()

@dp.message_handler(state=Bz_bn_aloqa.reply_to_message_id)
async def answer(message: Message,state: FSMContext):
    try:
        reply_to_msg_id = message.text
        await state.update_data(
            {"reply_to_msg_id": reply_to_msg_id}
        )
        data = await state.get_data()
        user_id = data.get("user_id")
        msg = data.get("msg_for_send_user")
        user_id = int(user_id)
        reply_to_msg_id = data.get("reply_to_msg_id")
        try:
            await dp.bot.send_audio(user_id, msg,reply_to_message_id=int(reply_to_msg_id))
            await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)
        except Exception:
            await dp.bot.send_message(user_id,f"<b>{msg}</b>",reply_to_message_id=int(reply_to_msg_id),parse_mode="HTML")
            await message.answer("Xabar muvoffaqiyatli yuborildi")
            await state.finish()
            await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)
    except Exception:
        pass

@dp.callback_query_handler(text_contains='delete')
async def answer(call: CallbackQuery):
    await call.message.delete()