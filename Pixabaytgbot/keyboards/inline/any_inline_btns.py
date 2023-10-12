from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


keyboard_for_aloqa = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Javob yozish 🚀",callback_data="answer_call"),
        InlineKeyboardButton(text="❌",callback_data="delete"),
        InlineKeyboardButton(text="Bloklash 🚫",callback_data="block_user")],
    ],
)

aloqa_btn_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Menda taklif bor 🤝",callback_data="taklif_bor")],
        [InlineKeyboardButton(text="Xatolik topdim ❗️",callback_data="xatolik_topdim")],
        [InlineKeyboardButton(text="Bekor qilish 🚫",callback_data="cancel")],
    ],
)

share = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ulashish 🚀", switch_inline_query="Islom dini uchun foydali va ma'lumotlarga boy bot ekan.\nBotga kiring, ishga tushuring va botning to'liq imkoniyatlari haqida botning o'zidan ma'lumot oling 😊")]
    ],
)


from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

btnshare =InlineKeyboardButton("Botni ulashish",url="https://t.me/py_pixabay_bot",callback_data="share")
btnsharemenu = InlineKeyboardMarkup().add(btnshare)

btnchangeconfig = InlineKeyboardButton(text="Qidirish sozlamalarini sozlash ⚙️",callback_data="changeconfig")
btnru = InlineKeyboardButton(text="Rus-tili 🇷🇺",callback_data="langru")
btnen = InlineKeyboardButton(text="Ingliz tili 🇺🇸",callback_data="langen")
btnde = InlineKeyboardButton(text="Nemis tili 🇩🇪",callback_data="langde")
btntr = InlineKeyboardButton(text="Turk tili 🇹🇷",callback_data="langtr")
btnko = InlineKeyboardButton(text="Koreys tili 🇰🇷",callback_data="langko")
btnit = InlineKeyboardButton(text="Italiya tili 🇮🇹",callback_data="langit")
btnfr = InlineKeyboardButton(text="Fransuz tili 🇫🇷",callback_data="langfr")
btnuz = InlineKeyboardButton(text="O'zbek tili 🇺🇿",callback_data="languz")

btn_category_fashion = InlineKeyboardButton(text="Moda 👗",callback_data="fashion")
btn_category_nature = InlineKeyboardButton(text="Tabiat 🏕",callback_data="nature")
btn_category_education = InlineKeyboardButton(text="Ta'lim 🎓",callback_data="education")
btn_category_science = InlineKeyboardButton(text="Ilm-Fan 📚",callback_data="science")
btn_category_health = InlineKeyboardButton(text="Sog'liq 🚑",callback_data="health")
btn_category_people = InlineKeyboardButton(text="Insonlar 🧍‍♂️🧍‍♀️",callback_data="people")
btn_category_religion = InlineKeyboardButton(text="Din 🕌",callback_data="religion")
btn_category_places = InlineKeyboardButton(text="Mashxur joylar 🪧",callback_data="places")
btn_category_animals = InlineKeyboardButton(text="Xayvonlar 🐻‍❄️",callback_data="animals")
btn_category_computer = InlineKeyboardButton(text="Texnologiya 👨🏻‍💻",callback_data="computer")
btn_category_music = InlineKeyboardButton(text="Musiqa 🎵",callback_data="music")
btn_category_travel = InlineKeyboardButton(text="Sayohat ✈️",callback_data='travel')
btn_category_buildings = InlineKeyboardButton(text="Qurilish 🏗",callback_data="buildings")
btn_category_business = InlineKeyboardButton(text="Biznez 🕴",callback_data="business")
btn_category_feelings = InlineKeyboardButton(text="Tuyg'ular 😊",callback_data="feelings")

btnpageone = InlineKeyboardButton(text="1️⃣",callback_data="page1")
btnpagetwo = InlineKeyboardButton(text="2️⃣",callback_data="page2")
btnpagethree = InlineKeyboardButton(text="3️⃣",callback_data="page3")
btn_per_pagetwenty = InlineKeyboardButton(text="2️⃣0️⃣",callback_data="per_page20")
btn_per_page_twohundred = InlineKeyboardButton(text="2️⃣0️⃣0️⃣",callback_data="per_page200")
btnorder = InlineKeyboardButton(text="Eng mashxurlar 🤩",callback_data="order_popular")
btnorderlatest = InlineKeyboardButton(text="Eng yangilari 🆕",callback_data="order_latest")
btnpic = InlineKeyboardButton(text="Rasm qidirish 🖼",callback_data="search_pic")
btnvid = InlineKeyboardButton(text="Video qidirish 🎥",callback_data="search_vid")

btnfilm = InlineKeyboardButton(text="Film 🎥",callback_data="film")
btnanimation = InlineKeyboardButton(text="Animatsiya 🎬",callback_data="animation")
btnall_type = InlineKeyboardButton(text="Barchasi",callback_data="all")
btnillustration = InlineKeyboardButton(text="Illustratsiya ✨",callback_data="illustration")
btnphoto = InlineKeyboardButton(text="Fotosurat 📸",callback_data="photo")


changemenu = InlineKeyboardMarkup().add(btnchangeconfig)

langmenu = InlineKeyboardMarkup().add(btnru,btnen).add(btntr,btnko).add(btnit,btnfr).row(btnde)

videotypemenu = InlineKeyboardMarkup().add(btnfilm,btnanimation).row(btnall_type)

image_type_menu = InlineKeyboardMarkup().add(btnillustration,btnphoto).row(btnall_type)

categorymenu = InlineKeyboardMarkup().add(btn_category_fashion,btn_category_nature,btn_category_health,btn_category_science,btn_category_education,btn_category_religion,btn_category_people,btn_category_places,btn_category_travel,btn_category_music,btn_category_computer,btn_category_buildings,btn_category_animals,btn_category_business,btn_category_feelings)

pagemenu = InlineKeyboardMarkup().add(btnpageone,btnpagetwo,btnpagethree)

perpagemenu = InlineKeyboardMarkup().add(btn_per_pagetwenty,btn_per_page_twohundred)

ordermenu = InlineKeyboardMarkup().add(btnorder,btnorderlatest)

searchmenu = InlineKeyboardMarkup().add(btnpic,btnvid)
