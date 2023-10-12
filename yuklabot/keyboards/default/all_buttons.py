from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📹 144p", callback_data="160"),
            InlineKeyboardButton("📹 240p", callback_data="133"),
            InlineKeyboardButton("📹 360p", callback_data="134"),
        ],
        [
            InlineKeyboardButton("📹 480p", callback_data="135"),
            InlineKeyboardButton("📹 720p", callback_data="136"),
            InlineKeyboardButton("📹 1080p", callback_data="137"),
        ],
        [
            InlineKeyboardButton("🔊 MP3", callback_data="audio_mp3"),
            InlineKeyboardButton("🖼", callback_data="thumbnail"),
            InlineKeyboardButton("Subtitle 📖", callback_data="subtitle"),
        ],
        [
            InlineKeyboardButton("Summary 🪄",callback_data="summary")
        ],
        [
            InlineKeyboardButton("Ortga 🔙",callback_data="back")
        ]
    ],
    row_width=3
)