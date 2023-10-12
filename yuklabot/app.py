from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await db.create()
    await db.create_table_users()
    await db.create_table_dailymotion()
    await db.create_table_facebook()
    await db.create_table_snapchat()
    await db.create_table_youtube_addition()
    await db.create_table_youtube_video()
    await db.create_table_pinterest()
    await db.create_table_twitter()
    await set_default_commands(dispatcher)


    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
