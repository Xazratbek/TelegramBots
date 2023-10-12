from aiogram.types import Message, ReplyKeyboardRemove, MediaGroup
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatActions
from loader import dp, db
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import requests
from aiogram.dispatcher.filters import Text
import os
import time
from io import BytesIO

@dp.message_handler(Text(contains='https://www.instagram.com',ignore_case=True))
async def handle_instagram_post(message: Message, state: FSMContext):
    await message.answer("Video yuklanmoqda iltimos biroz kuting")
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://snapinsta.app/')
    input = driver.find_element(By.XPATH,'//*[@id="url"]')
    input.send_keys(message.text)
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="downloader"]/form/button').click()
    time.sleep(3)
    div_elements = driver.find_elements(By.CLASS_NAME,'download-bottom')
    print(len(div_elements))

    hrefs_dict = {}
    for div_element in range(len(div_elements)):
        a_tag = div_elements[div_element].find_element(By.TAG_NAME, 'a')
        text = a_tag.text
        href = a_tag.get_attribute('href')
        hrefs_dict[text] = href
    print(len(hrefs_dict))

    # if len(hrefs_dict) == 1:
    #     buffer = BytesIO()
    #     res = requests.get(hrefs_dict[list(hrefs_dict.keys())[0]])

    #     buffer.write(res.content)
    #     buffer.seek(0)
    #     if list(hrefs_dict.keys())[0] == "Download Video":
    #         await message.answer_video(buffer)
    #     else:
    #         await message.answer_photo(buffer)

    # else:
    path = 'D:/Programming projects/Telegram bots/yuklabot/media/instagram'
    album = MediaGroup()
    for text, href in hrefs_dict.items():
        print(f"{href}\n\n")
        buffer = BytesIO()
        res = requests.get(href)
        buffer.write(res.content)
        buffer.seek(0)
        if "Download Video" in text:
            album.attach_video(buffer)
        else:
            album.attach_photo(buffer)
    await message.answer_media_group(album)
    driver.quit()
