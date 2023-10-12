from aiogram.types import ChatActions
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from states.button_state import Button, ChooseLanguage
from keyboards.default.main_menu import main_menu, source_language_keyboard, desired_language_keyboard
from function import shoki_app
import time
import re
from docx import Document
import os



@dp.message_handler(text_contains="Video transcript 🎬 📝")
async def answer(message: Message, state: FSMContext):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    await Button.button.set()
    await state.update_data(
    {
        "get" : '//*[@id="__next"]/div/div[2]/div[4]/button[2]'
    })
    await ChooseLanguage.source_language.set()
    await message.answer("Videoning tilini tanlang",reply_markup=source_language_keyboard)

@dp.message_handler(text_contains="Ortga 🔙",state=Button.button)
async def ortga(message: Message, state: FSMContext):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    time.sleep(1)
    await state.finish()
    await message.answer("Siz asosiy menudasiz",reply_markup=main_menu)

@dp.message_handler(text_contains="Video summary 🎬 🧐📝")
async def answer(message: Message, state: FSMContext):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    await Button.button.set()
    await state.update_data(
    {
        "get" : '//*[@id="__next"]/div/div[2]/div[4]/button[1]'
    })
    await ChooseLanguage.source_language.set()
    await message.answer("Videoni tilini tanlang",reply_markup=source_language_keyboard)

@dp.message_handler(state=ChooseLanguage.source_language)
async def source_language(message: Message,state: FSMContext):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    time.sleep(1)
    if message.text in ["🇦🇪 Arabic","🇨🇳 Chinese","🇬🇧 English","🇫🇷 French","🇩🇪 German","🇮🇳 Hindi","🇯🇵 Japanese","🇰🇷 Korean","🇵🇹 Portuguese","🇷🇺 Russian","🇪🇸 Spanish","🇹🇷 Turkish"]:
        await state.update_data(
            {
                "source_language" : message.text.split()[-1]
            }
        )
        await ChooseLanguage.desire_language.set()
        await message.answer("Matnni boshqa tilga tarjima qilmoqchi bo'lsangiz pastdagi tillardan birini tanlang yoki videni o'zini tilini tanlang",reply_markup=desired_language_keyboard)
    else:
        await message.answer("Iltimos pastdagi tugmalardan birini tanlang")

@dp.message_handler(text_contains="Ortga 🔙",state=ChooseLanguage.source_language)
async def ortga(message: Message, state: FSMContext):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    time.sleep(1)
    await Button.button.set()
    await message.answer("Pastdagi tugmalardan birini tanlang",reply_markup=main_menu)

@dp.message_handler(text_contains="Ortga 🔙",state=ChooseLanguage.desire_language)
async def ortga(message: Message, state: FSMContext):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    time.sleep(1)
    await ChooseLanguage.source_language.set()
    await message.answer("Videoni tilini tanlang",reply_markup=source_language_keyboard)

@dp.message_handler(state=ChooseLanguage.desire_language)
async def get_answer(message: Message, state: FSMContext):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    if message.text in ["🇦🇪 Arabic","🇨🇳 Chinese","🇬🇧 English","🇫🇷 French","🇩🇪 German","🇮🇳 Hindi","🇯🇵 Japanese","🇰🇷 Korean","🇵🇹 Portuguese","🇷🇺 Russian","🇪🇸 Spanish","🇹🇷 Turkish"]:
        await state.update_data(
            {
                "desire_language" : message.text.split()[-1]
            }
        )
        await ChooseLanguage.youtube_url.set()
        await message.answer("YouTube video urlni yuboring",reply_markup=ReplyKeyboardRemove())

    else:
        await message.answer("Iltimos pastdagi tugmalardan birini tanlang")

@dp.message_handler(state=ChooseLanguage.youtube_url)
async def send_data(message: Message, state: FSMContext):
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    time.sleep(1)
    data = await state.get_data()
    get = data.get("get")
    source_language = data.get("source_language")
    desire_language = data.get("desire_language")
    print(desire_language)
    print(source_language)
    # match = re.match(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/watch\?v=([A-Za-z0-9_-]{11})',message.text)
    # if match:
    msg = await message.answer("📝")
    data = await shoki_app(source_language,desire_language,get,message.text)
    if len(data) <= 3000:
        await dp.bot.delete_message(message.from_user.id,msg.message_id)
        await message.answer(data)
        await state.finish()
        await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)
    else:
        doc = Document()
        doc.add_paragraph(data)
        doc.save("result.docx")
        await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.UPLOAD_DOCUMENT)
        time.sleep(1)
        with open('result.docx','rb') as file:
            await message.answer_document(file)
            await state.finish()
            os.remove('result.docx')
            await message.answer("Siz asosiy menuga qaytdingiz",reply_markup=main_menu)
    # else:
    #     await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.TYPING)
    #     time.sleep(1)
    #     await message.answer("Iltimos youtube video url yuboring")