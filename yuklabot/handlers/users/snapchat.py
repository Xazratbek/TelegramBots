from aiogram.types import Message
from aiogram.types import ChatActions
from loader import dp, db
from aiogram.dispatcher.filters import Text
import yt_dlp
import os

@dp.message_handler(Text(contains='snapchat.com',ignore_case=True))
@dp.message_handler(Text(contains='spotlight',ignore_case=True))
async def send_video(message: Message):
    if await db.check_availabilaty_snapchat(message.text):
        data = await db.get_snapchat_media(message.text)
        await message.answer_video(data[0]['file_id'])
        return
    msg = await message.answer("Video yuklanmoqda biroz kuting")
    ydl = yt_dlp.YoutubeDL()
    output_directory = r'D:\Programming projects\Telegram bots\yuklabot\media\snapchat'
    output_filename = 'downloaded_video.mp4'

    # Create the full output path
    output_path = os.path.join(output_directory, output_filename)
    directory_path = r'D:\Programming projects\Telegram bots\yuklabot'

    ydl = yt_dlp.YoutubeDL()

    # URL of the Snapchat video


    # Options for downloading the video (you can customize these)
    options = {
        'format': 'best',
        'outtmpl': 'downloaded_video.mp4',  # Output file name
    }

    try:
        with ydl:
            result = ydl.extract_info(message.text, download=True, extra_info=options)
            contents = os.listdir(directory_path)
            snap = contents[12]
            full_current_path = os.path.join(directory_path, snap)

            # Specify the new filename
            new_filename = 'video.mp4'

            # Construct the full path to the new filename
            full_new_path = os.path.join(directory_path, new_filename)

            # Rename the file
            os.rename(full_current_path, full_new_path)
            await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.UPLOAD_VIDEO)
            with open('video.mp4','rb') as media:
                video = await message.answer_video(media)
                await dp.bot.delete_message(message.from_user.id,msg.message_id)
                await db.add_snapchat_media(message.text,video['video']['file_id'])
                if os.path.exists('video.mp4'):
                    os.remove('video.mp4')

    except Exception as e:
        print(e)
        await message.answer("Uzur videoni yuklab bo'lmadi")