from aiogram.dispatcher.filters.state import StatesGroup, State

class DeclinePostState(StatesGroup):
    declined_user_id = State()
    moder_id = State()
    decline_reason = State()


class ReportAnswerState(StatesGroup):
    answer = State()
