from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot, config

@dp.message_handler(chat_id=config['ADMINS'], commands=['state'])
async def process_admin_command_state(message: types.Message, state: FSMContext):
    await state.update_data(prev_command='state')
    data = await state.get_data()
    await message.answer(data['prev_command'])
