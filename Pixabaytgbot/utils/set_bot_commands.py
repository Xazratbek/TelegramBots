from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni qayta ishga tushurish ♻️"),
            types.BotCommand("help", "Yordam olish 🆘"),
            types.BotCommand("info","Bot imkoniyatlari haqida ma'lumot olish ✅")
        ]
    )
