from aiogram.types import Message
from loader import dp, db
from aiogram.dispatcher.filters import Text
import os
from io import BytesIO
import yt_dlp

@dp.message_handler(Text(contains='dailymotion.com',ignore_case=True))
async def download_twitter_video(message: Message):
    if await db.check_availabilaty_dailymotion(message.text):
        data = await db.get_dailymotion_media(message.text)
        await message.answer_video(data[0]['file_id'])
        return
    buffer = BytesIO()
    msg = await message.answer("Video yuklanmoqda biroz kuting")
    ydl_opts = {
        'format': 'best',  # Choose the best available quality
        'outtmpl': '%(title)s.%(ext)s',  # Output file name format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # try:
        info_dict = ydl.extract_info(message.text, download=False)
        # Specify a default extension for the video format
        default_extension = 'mp4'
        # Determine the extension to use (fallback to the default if not present)
        ext = info_dict.get('ext', default_extension)
        # Open the downloaded file and read its contents
        with open(f"{info_dict['title']}.{ext}", 'rb') as video_file:
            video_data = video_file.read()
        # Write the video data to the BytesIO buffer
        buffer.write(video_data)
        buffer.seek(0)
        # Send the video from the BytesIO buffer
        await message.answer_video(video=buffer)
        # except Exception as e:
        #     print(e)
        #     print(f"An error occurred: {str(e)}")
            # contents = os.listdir(directory_path)
            # first_item = contents[0]
            # full_current_path = os.path.join(directory_path, first_item)
            # # Specify the new filename
            # new_filename = 'video.mp4'
            # # Construct the full path to the new filename
            # full_new_path = os.path.join(directory_path, new_filename)
            # # Rename the file
            # os.rename(full_current_path, full_new_path)
            # with open(f'{directory_path}video.mp4','rb') as media:
            #     video = await message.answer_video(media)
            #     await dp.bot.delete_message(message.from_user.id,msg.message_id)
            #     await db.add_dailymotion_media(message.text,video['video']['file_id'])
            #     if os.path.exists(f'{directory_path}video.mp4'):
            #         os.remove(f'{directory_path}video.mp4')
        # except Exception as e:
        #     print("Salom")
