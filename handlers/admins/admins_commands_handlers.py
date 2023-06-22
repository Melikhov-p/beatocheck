from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot, config

@dp.message_handler(chat_id=config['SUPERUSER_ID'], commands=['state'])
async def process_admin_command_state(message: types.Message, state: FSMContext):
    await state.update_data(prev_command='state')
    data = await state.get_data()
    await message.answer(data['prev_command'])


@dp.message_handler(chat_id=config['SUPERUSER_ID'], commands=['moders_alert'])
async def process_admin_command_moders_alert(message: types.Message):
    await bot.send_message(config['MODERS_CHAT'], f'{message.get_args()}'.upper(), parse_mode='html')
