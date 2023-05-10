from aiogram.dispatcher import FSMContext

from keyboards.reply_keyboards import cancel_kb
from loader import dp, bot
from states.BasicStates import BuyBeatState
from aiogram import types


# --- СЦЕНАРИЙ ПОКУПКИ БИТА ---
@dp.callback_query_handler(lambda c: c.data == 'buy_beat_btn')
async def process_buy_beat_btn(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, "Чтобы купить бит сначала отправь <b>id бита</b>:\n\n\n", parse_mode='html', reply_markup=cancel_kb)
    await BuyBeatState.beat_id.set()


@dp.message_handler(state=BuyBeatState.beat_id, content_types=['text'])
async def get_beat_id(message: types.Message, state: FSMContext):
    beat_id = message.text
    await state.update_data(beat_id=beat_id)
    await bot.send_message(message.from_user.id, f'BEAT: {beat_id}')
    await state.finish()

# --- КОНЕЦ СЦЕНАРИЯ ПОКУПКИ БИТА ---
