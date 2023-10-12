import logging
from keyboards.default.many_buttons import main_menu_btn
from aiogram import types
from data.config import CHANNELS
from keyboards.inline.subscription import check_button
from loader import bot, dp
from utils.misc import subscription

@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
#     channels_format = str()
#     for channel in CHANNELS:
#         chat = await bot.get_chat(channel)
#         invite_link = await chat.export_invite_link()
#         logging.info(invite_link)
#         channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

#     await message.answer(f"Botdan bepul va cheklovlarsiz foydalanish uchun quyidagi kanalga obuna bo'ling: \n\n"
#                          f"{channels_format}",
#                          reply_markup=check_button,
#                          disable_web_page_preview=True)

# @dp.callback_query_handler(text="check_subs")
# async def checker(call: types.CallbackQuery):
#     await call.answer()
#     await call.message.delete()
#     callback_data = call.data
#     logging.info(f"{callback_data=}")
#     logging.info(f"{call.from_user.username=}")
#     result = str()
#     for channel in CHANNELS:
#         status = await subscription.check(user_id=call.from_user.id,
#                                           channel=channel)
#         channel = await bot.get_chat(channel)
#         if status:
#             result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n"
#         else:
#             invite_link = await channel.export_invite_link()
#             result2 = f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "\
#                        f"<a href='{invite_link}'>-ga Obuna bo'ling</a>\n\n"
#     if status:
    await message.answer(f"Salom {message.from_user.id}",reply_markup=main_menu_btn)
    # else:
    #     await call.message.answer(result2, disable_web_page_preview=True)
