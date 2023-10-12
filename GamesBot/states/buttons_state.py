from aiogram.dispatcher.filters.state import State, StatesGroup

class TrackUser(StatesGroup):
    part = State()
    game_name = State()