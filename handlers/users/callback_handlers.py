from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.reply_keyboards import cancel_kb
from loader import dp, bot, config
from aiogram import types
from keyboards.inline_keyboards import inline_menu_kb
from states.BasicStates import ReportState

# Основные колбэки
@dp.callback_query_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), lambda callback: callback.data == 'menu_btn')
async def process_callback_menu_btn(callback: types.CallbackQuery):
    await callback.message.edit_text(f'<b>Основное меню</b>\n\n'
                                     f'Что тебя интересует?', parse_mode='html')
    await callback.message.edit_reply_markup(inline_menu_kb)

@dp.callback_query_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), lambda callback: callback.data == 'menu_report_btn')
async def process_callback_report_btn(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Опиши свою проблему: ', reply_markup=cancel_kb)
    await ReportState.report.set()
@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), state=ReportState.report)
async def process_callback_send_report(message: types.Message):
    await bot.send_message(config['MODERS_CHAT'], f'🔴REPORT🔴\n\n'
                                                  f'ОТ: @{message.from_user.username} | user_id: {message.from_user.id}\n'
                                                  f'ТЕКСТ: {message.text}', parse_mode='html', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Ответить', callback_data='answer_to_report')))

@dp.callback_query_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), lambda callback: callback.data == 'menu_info_btn')
async def process_callback_info_btn(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Все основные команды есть в левом нижнем углу чата.\n\n'
                                                  'Кнопки меню:\n'
                                                  ' <b>-<u>Отправить бит</u></b>: запускает сценарий создания поста с твоим битом.\n'
                                                  ' <b>-<u>Как купить бит</u></b>: инструкция покупки.\n'
                                                  ' <b>-<u>Правила</u></b>: правила канала @beatocheck.\n'
                                                  ' <b>-<u>Возникли проблемы</u></b>: отправить репорт с возникшей проблемой.\n\n'
                                                  '🔴 <b>Обрати внимание</b>, во время выполнения любого из сценариев, остальные возможности бота будут отключены, чтобы отменить сценарий отправь команду /cancel,'
                                                  ' или нажми соответствующую кнопку в контекстном меню бота.', parse_mode='html')


@dp.callback_query_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), lambda callback: callback.data == 'menu_rules_btn')
async def process_callback_rules_btn(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Основное правило - <b>бит должен быть твоим</b>, если будешь использовать чужие биты, будешь исключен из группы и потеряешь доступ к боту <u>навсегда</u>.', parse_mode='html')


# Callback для жалобы из канала на пост
@dp.callback_query_handler(lambda callback: callback.data == 'report_for_post', chat_id=config['CHANNEL_ID'])
async def process_callback_report_for_post(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Напиши мне /report <ссылка на пост> и что именно тебя не устраивает, мы обязательно разберемся.')
