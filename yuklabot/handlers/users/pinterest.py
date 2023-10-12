from aiogram.types import Message
from aiogram.types import ChatActions
from loader import dp, db
from aiogram.dispatcher.filters import Text
import yt_dlp
import os
import subprocess

@dp.message_handler(Text(contains='pinterest.com',ignore_case=True))
@dp.message_handler(Text(contains='pin.it',ignore_case=True))
async def send_video(message: Message):
    if await db.check_availabilaty_pinterest(message.text):
        data = await db.get_pinterest_media(message.text)
        await message.answer_photo(data[0]['file_id'])
        return
    msg = await message.answer("Yuklanmoqda biroz kuting ⏳")
    command = ["python","D:\Programming projects\Telegram bots\yuklabot\pin_down.py", "-rs", message.text]

    try:
        # Run the command

        result = subprocess.run(command, check=True, shell=True)
        directory_path = "D:/Programming projects/Telegram bots/yuklabot/images"
        contents = os.listdir(directory_path)
        pin = contents[0]
        log = contents[1]
        full_current_path = os.path.join(directory_path, pin)
        # Specify the new filename
        new_filename = 'image.jpg'
        # Construct the full path to the new filename
        full_new_path = os.path.join(directory_path, new_filename)
        # Rename the file
        os.rename(full_current_path, full_new_path)
        with open(f"{directory_path}/image.jpg",'rb') as media:
            image = await message.answer_photo(media)
            await db.add_pinterest_media(message.text,image['photo'][-1]['file_id'])
            if os.path.exists(f"{directory_path}\image.jpg"):
                os.remove(f"{directory_path}\image.jpg")
                os.remove(f"{directory_path}\{log}")

    except subprocess.CalledProcessError as e:
        await message.answer("Uzur nimadur xato ketdi, qayta urunib ko'ring")
