from aiogram.dispatcher.filters.state import StatesGroup, State


# Состояния
# Создание бита на пост
class BeatState(StatesGroup):
    author = State()
    title = State()
    tags = State()
    tagged_beat = State()
    price = State()
    cover = State()
    confirm = State()


class ReportState(StatesGroup):
    report = State()
