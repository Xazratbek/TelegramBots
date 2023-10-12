from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, WebAppInfo

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("shoki.app web",web_app=WebAppInfo(url="https://shoki.app/"))
        ],
        [
            KeyboardButton("Video transcript 🎬 📝")
        ],
        [
            KeyboardButton("Video summary 🎬 🧐📝")
        ],
    ],
    resize_keyboard=True
)


language_options = [
    "🇦🇪 Arabic",
    "🇨🇳 Chinese",
    "🇬🇧 English",
    "🇫🇷 French",
    "🇩🇪 German",
    "🇮🇳 Hindi",
    "🇯🇵 Japanese",
    "🇰🇷 Korean",
    "🇵🇹 Portuguese",
    "🇷🇺 Russian",
    "🇪🇸 Spanish",
    "🇹🇷 Turkish"
]

# Create a ReplyKeyboardMarkup for source language
source_language_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

# Create a ReplyKeyboardMarkup for desired language
desired_language_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

# Add buttons for each language option to source_language_keyboard
for language_option in language_options:
    source_language_keyboard.add(KeyboardButton(text=language_option))
source_language_keyboard.add(KeyboardButton(text="Ortga 🔙"))

# Add buttons for each language option to desired_language_keyboard
for language_option in language_options:
    desired_language_keyboard.add(KeyboardButton(text=language_option))

desired_language_keyboard.add(KeyboardButton(text="Ortga 🔙"))