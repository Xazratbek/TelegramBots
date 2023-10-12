from aiogram.types import Message
from aiogram.types import ChatActions
from loader import dp, db
from aiogram.dispatcher.filters import Text
import os
import subprocess

@dp.message_handler(Text(contains='twitter.com',ignore_case=True))
@dp.message_handler(Text(contains='x.com',ignore_case=True))
async def download_twitter_video(message: Message):
    if await db.check_availabilaty_x(message.text):
        data = await db.get_twitter_media(message.text)
        await message.answer_video(data[0]['file_id'])
        return
    msg = await message.answer("Video yuklanmoqda biroz kuting")
    await dp.bot.send_chat_action(chat_id=message.from_user.id,action=ChatActions.UPLOAD_VIDEO)
    command = ["yt-dlp", message.text]
    directory_path = r'D:\Programming projects\Telegram bots\yuklabot\media\twitter'

    output_directory = "D:/Programming projects/Telegram bots/yuklabot/media/twitter"
    filename_template = "%(title)s.%(ext)s"
    command += ["-o", f"{output_directory}/{filename_template}"]

    # Run the command
    try:
        subprocess.run(command, check=True, shell=True)
        contents = os.listdir(directory_path)
        first_item = contents[0]
        full_current_path = os.path.join(directory_path, first_item)

        # Specify the new filename
        new_filename = 'video.mp4'

        # Construct the full path to the new filename
        full_new_path = os.path.join(directory_path, new_filename)

        # Rename the file
        os.rename(full_current_path, full_new_path)
        with open(f'D:/Programming projects/Telegram bots/yuklabot/media/twitter/video.mp4','rb') as media:
            video = await message.answer_video(media)
            await dp.bot.delete_message(message.from_user.id,msg.message_id)
            await db.add_x_media(message.text,video['video']['file_id'])
            if os.path.exists('D:/Programming projects/Telegram bots/yuklabot/media/twitter/video.mp4'):
                os.remove('D:/Programming projects/Telegram bots/yuklabot/media/twitter/video.mp4')

    except subprocess.CalledProcessError as e:
        await message.answer("Iltimos twitter videoning urlini yuboring")
