# from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
# from aiogram.dispatcher.filters import Command
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ChatActions
# from loader import dp, db, bot
# from aiogram.dispatcher.filters import Text
# from states.youtube_state import YtVideoQuality
# import requests
# from bs4 import BeautifulSoup
# from docx import Document
# from io import BytesIO
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from pytube import YouTube
# from keyboards.default.all_buttons import inline_keyboard

# # @dp.message_handler(Text(contains="https://youtube.com",ignore_case=True))
# # @dp.message_handler(Text(contains="https://youtu.be",ignore_case=True))

# @dp.message_handler()
# async def choose_resolution(message: Message, state: FSMContext):
#     yt = YouTube(message.text)
#     if yt.check_availability() is None:
#         pass
#     else:
#         await message.answer("Iltimos youtube video yuboring")

#     thumbnail_url = yt.thumbnail_url
#     title = yt.title
#     author = yt.author
#     video_streams = yt.streams.filter(progressive=True).order_by("resolution").desc()
#     sizes = "\n".join([f"🚀 {stream.resolution}: {stream.filesize/1024/1024:.2f}MB" for stream in video_streams])
#     caption = f"👤 #{author}\n\n📝 {title} [{author}]\n\n{sizes}\n\nVideo yuklab olish formatlari 👇"
#     await message.answer_photo(thumbnail_url,caption=caption,reply_markup=inline_keyboard)
#     await YtVideoQuality.video_quality.set()
#     await state.update_data(
#         {
#             "video_url" : message.text
#         }
#     )

# @dp.callback_query_handler(state=YtVideoQuality.video_quality,text_contains="back")
# async def answer(call: CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     await state.finish()
#     await call.message.answer("Siz asosiy menyudasiz")

# @dp.callback_query_handler(state=YtVideoQuality.video_quality)
# async def process_callback(call: CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     video_url = data.get("video_url")

#     await call.message.delete()
#     buffer=BytesIO()

#     yt = YouTube(video_url)
#     filename=yt.title
#     try:
#         if call.data.isdigit():
#             itag = int(call.data)
#             if await db.check_availabilaty_youtube_video(video_url,int(call.data)):
#                 data = await db.get_youtube_video_media(video_url,int(call.data))
#                 await call.message.answer_video(data[0]['file_id'])
#                 return

#             stream = yt.streams.get_by_itag(itag)
#             stream.stream_to_buffer(buffer=buffer)
#             if stream:
#                 await dp.bot.send_chat_action(chat_id=call.message.from_user.id,action=ChatActions.UPLOAD_VIDEO)
#                 buffer.seek(0)
#                 video = await bot.send_video(call.message.from_user.id, video=buffer,caption=filename)
#                 await db.add_youtube_video_media(video_url,video['video']['file_id'],itag)
#                 await state.finish()
#                 await call.message.answer("Siz asosiy menyuga qaytdingiz")
#             else:
#                 await bot.send_message(call.message.from_user.id, "Videoning bu sifati mavjud emas iltimos boshqa sifatni tanlang")


        # elif call.data == "audio_mp3":
        #     if await db.check_availabilaty_youtube_addition_audio(video_url,'true')['available']:
        #         data = await db.get_youtube_addition_media_audio(video_url)
        #         await call.message.answer_audio(data['data'][0]['file_id'],caption=yt.title)
        #         return

        #     msg = await call.message.answer("Audio yuklanmoqda iltimos biroz kuting ⏳")
        #     audio=yt.streams.get_audio_only()
        #     await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.UPLOAD_AUDIO)
        #     audio.stream_to_buffer(buffer=buffer)
        #     buffer.seek(0)
        #     audio = await call.message.answer_audio(audio=buffer,caption=filename)
        #     await db.add_youtube_addition_media(video_url,audio['audio']['file_id'],'true','false','false','false')
        #     await state.finish()
        #     await call.message.answer("Siz asosiy menyuga qaytdingiz")
        #     # audio['voice']['file_id']

#         elif call.data == "thumbnail":
#             if await db.check_availabilaty_youtube_addition_thumbnail(video_url,'true')['available']:
#                 data = await db.check_availabilaty_youtube_addition_thumbnail(video_url,'true')
#                 await call.message.answer_video(data['data']['data'][0]['file_id'])
#                 return

#             thumbnail_url = yt.thumbnail_url

#             if thumbnail_url:
#                 photo = await bot.send_photo(call.message.from_user.id, thumbnail_url, caption=yt.title)
#                 await db.add_youtube_addition_media(video_url,photo['photo']['file_id'],'false','true','false','false')
#                 await state.finish()
#                 await call.message.answer("Siz asosiy menyuga qaytdingiz")
#             else:
#                 await call.answer("Thumbnail is not available")

#         elif call.data == "subtitle":
#             captions = yt.captions.all()

#             if captions:
#                 # Choose the first available subtitle track
#                 subtitle_track = captions[0]
#                 subtitle_text = subtitle_track.generate_srt_captions()

#                 if subtitle_text:
#                     doc = Document()
#                     doc.add_paragraph(subtitle_text)
#                     doc.save("captions.docx")
#                     await dp.bot.send_chat_action(call.message.from_user.id,action=ChatActions.UPLOAD_DOCUMENT)
#                     doc_bytes_io = BytesIO()
#                     doc.save(doc_bytes_io)

#                     # Reset the file pointer to the beginning of the BytesIO object
#                     doc_bytes_io.seek(0)

#                     # Send the document as a file to the user
#                     document = await bot.send_document(call.message.from_user.id,doc_bytes_io,caption=yt.title)
#                     await db.add_youtube_addition_media(video_url,document['document']['file_id'],'false','false','false','true')
#                     await state.finish()
#                     await call.message.answer("Siz asosiy menyuga qaytdingiz")

#                 else:
#                     await bot.send_message(call.message.from_user.id, "Subtitle track is empty.")
#             else:
#                 await call.answer("No subtitles available")



#     except Exception as e:
#         print(e)
