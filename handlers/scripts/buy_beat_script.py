from aiogram.dispatcher import FSMContext

from keyboards.reply_keyboards import cancel_kb
from loader import dp, bot
from aiogram import types


# --- СЦЕНАРИЙ ПОКУПКИ БИТА ---
@dp.callback_query_handler(lambda c: c.data == 'buy_beat_btn')
async def process_buy_beat_btn(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, "Для покупки бита ты можешь связаться напрямую с автором, ссылка на автора <u>всегда</u> есть в посту канала @beatocheck", parse_mode='html', reply_markup=cancel_kb)
# --- КОНЕЦ СЦЕНАРИЯ ПОКУПКИ БИТА ---
