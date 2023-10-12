from aiogram.dispatcher.filters.state import StatesGroup, State

class Button(StatesGroup):
    button = State()

class ChooseLanguage(StatesGroup):
    source_language = State()
    desire_language = State()
    youtube_url = State()