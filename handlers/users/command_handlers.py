from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.dispatcher import FSMContext
from loader import dp, bot, config
from aiogram import types
from keyboards.inline_keyboards import inline_enter_kb, inline_menu_kb, inline_kb2


# Основные команды
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state='*', commands='cancel')  # команда для отмены процесса создания бита или покупки
async def process_cancel_command(message: types.Message, state: FSMContext):
    await state.finish()
    await process_callback_menu_command(message)


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"<b>Beat'o'check BOT</b>\n\n"
                                                 f" ⏩Выстави на продажу свой бит в пару кликов\n\n"
                                                 f" ⏩Купи интересующий тебя инструментал", parse_mode='html', reply_markup=inline_enter_kb)


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['menu'])
async def process_callback_menu_command(message: types.Message):
    await bot.send_message(message.from_user.id, f'<b>Основное меню</b>\n\n'
                                                 f'Что тебя интересует?', parse_mode='html', reply_markup=inline_menu_kb)


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['report'])
async def process_report_command(message: types.Message):
    args = message.get_args()
    await bot.send_message(config['MODER_CHAT'], f'REPORT\n'
                                                 f'ОТ: @{message.from_user.username} ({message.from_user.id})\n'
                                                 f'ТЕКСТ: {args}')
    await message.answer('Репорт отправлен, с вами свяжутся для решения проблемы.')
    await process_callback_menu_command(message)


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['test'])
async def process_test_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'test', reply_markup=inline_kb2)
