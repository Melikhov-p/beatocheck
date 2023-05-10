from aiogram.dispatcher.filters.state import StatesGroup, State


# Состояния
class BeatState(StatesGroup):
    author = State()
    title = State()
    tags = State()
    tagged_beat = State()
    price = State()
    cover = State()
    confirm = State()

class BuyBeatState(StatesGroup):
    beat_id = State()
