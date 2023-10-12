from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatActions
from loader import dp, db
import requests
from aiogram.dispatcher.filters import Text
import os
import yt_dlp

@dp.message_handler(Text(contains='https://www.facebook.com/',ignore_case=True))
@dp.message_handler(Text(contains=['videos','facebook','reel'],ignore_case=True))
async def handle_facebook_post(message: Message, state: FSMContext):
    # await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.UPLOAD_VIDEO)
    facebook_url = message.text
    if await db.check_availabilaty_fb(facebook_url):
        data = await db.get_facebook_media(facebook_url)
        await message.answer_video(data[0]['file_id'],reply_markup=ReplyKeyboardRemove())
        return

    msg = await message.answer("Video yuklanmoqda biroz kuting")
    directory_path = "D:/Programming projects/Telegram bots/yuklabot/media/facebook"
    ydl_opts = {
        'format': 'best',  # Choose the best available quality
        'outtmpl': f'{directory_path}/%(title)s.%(ext)s',  # Output file name format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([message.text])

            contents = os.listdir(directory_path)
            first_item = contents[0]
            full_current_path = os.path.join(directory_path, first_item)
            # Specify the new filename
            new_filename = 'video.mp4'
            # Construct the full path to the new filename
            full_new_path = os.path.join(directory_path, new_filename)
            # Rename the file
            os.rename(full_current_path, full_new_path)
            with open(f'{directory_path}/video.mp4','rb') as media:
                video = await message.answer_video(media)
                await dp.bot.delete_message(message.from_user.id,msg.message_id)
                await db.add_fb_media(message.text,video['video']['file_id'])
                if os.path.exists(f'{directory_path}/video.mp4'):
                    os.remove(f'{directory_path}/video.mp4')

        except Exception as e:
            await message.answer("Uzur videoni yuklab bo'lmadi, qayta urunib ko'ring")
