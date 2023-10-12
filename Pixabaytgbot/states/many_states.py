from aiogram.dispatcher.filters.state import StatesGroup, State

class Aloqa(StatesGroup):
    aloqa = State()

class Xatolik_topdim(StatesGroup):
    xatolik = State()

class Taklif_bor(StatesGroup):
    taklif = State()

class Bz_bn_aloqa(StatesGroup):
    user_id = State()
    msg = State()
    reply_to_message_id = State()

class Payments(StatesGroup):
    payments = State()

# class Search_img(StatesGroup):
#     Language = State()
#     Category = State()
#     Page = State()
#     Per_page = State()
#     New_or_famous = State()

# class Search_video(StatesGroup):
#     Category = State()
#     Page = State()
#     Per_page = State()
#     New_or_famous = State()
#     Type__of_video = State()

class TextForSearchPhoto(StatesGroup):
    text = State()

class TextForSearchVideo(StatesGroup):
    video = State()

class Results_for_video(StatesGroup):
    number = State()

class Results(StatesGroup):
    number = State()