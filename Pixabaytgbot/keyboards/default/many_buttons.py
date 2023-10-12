from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Rasm qidirish 🔎 🖼")],
        [KeyboardButton(text="Video qidirish 🔎 🎦")],
        [KeyboardButton(text="Biz bilan aloqa 💌")],
        [KeyboardButton(text="Botni ulashish 🚀")],
        [KeyboardButton(text="Loyihani qo'llab quvvatlash 💳 💲")],
    ],
    resize_keyboard=True
)

cancel_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bekor qilish 🚫")]
        ],
        resize_keyboard=True
)

tolov_tizimlari = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="CLICK ilovasi 💠")],
        [KeyboardButton(text="Payme ilovasi 📱")],
        [KeyboardButton(text="Apelsin ilovasi 🍊")],
        [KeyboardButton(text="Karta raqam orqali 💳")],
        [KeyboardButton(text="Ortga 🔙")],
    ],
    resize_keyboard=True,
)

results = ReplyKeyboardMarkup(
    keyboard=[
         [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
        ],
        [
            KeyboardButton(text="6"),
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9"),
            KeyboardButton(text="10"),
        ],
        [
            KeyboardButton(text="11"),
            KeyboardButton(text="12"),
            KeyboardButton(text="13"),
            KeyboardButton(text="14"),
            KeyboardButton(text="15"),
        ],
        [
            KeyboardButton(text="16"),
            KeyboardButton(text="17"),
            KeyboardButton(text="18"),
            KeyboardButton(text="19"),
            KeyboardButton(text="20"),
        ],
        [
            KeyboardButton(text="⬅️"),
            KeyboardButton(text="❌"),
            KeyboardButton(text="➡️"),
        ],
    ],
    resize_keyboard=True,
)