from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot, config
from aiogram import types
import re
from states.ModerChatStates import DeclinePostState, ReportAnswerState


# Callback's модерации поста
@dp.callback_query_handler(lambda callback: callback.data == 'admin_accept_post')
async def process_callback_accept_post_to_channel(callback: types.CallbackQuery):
    audio_id = re.findall(r'audio:.*', callback.message.caption)[0].replace('audio:', '')  # id файла с аудио из сообщения
    user_id = re.findall(r'user_id:.*', callback.message.caption)[0].replace('user_id:', '')
    callback.message.caption = re.sub(r'audio:.*', '', callback.message.caption)
    callback.message.caption = re.sub(r'user_id:.*', '', callback.message.caption)
    await callback.message.edit_caption(f'{callback.message.caption}\n--------------------\n✅ОДОБРЕНА✅', parse_mode='html')
    await bot.send_message(user_id, 'Твой бит одобрен к размещению, он уже в канале @beatocheck')  # Сообщение юзеру что бит одобрен
    await bot.send_photo(config['CHANNEL_ID'], photo=callback.message.photo[-1].file_id, caption=callback.message.caption.replace('@ ', '@'), parse_mode='html')
    await bot.send_audio(config['CHANNEL_ID'], audio=audio_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Пожаловаться', callback_data='report_for_post')))


@dp.callback_query_handler(lambda callback: callback.data == 'admin_decline_post')
async def process_callback_decline_post_to_channel(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(declined_user_id=re.findall(r'user_id:.*', callback.message.caption)[0].replace('user_id:', ''))
    await state.update_data(moder_id=callback.from_user.id)
    callback.message.caption = re.sub(r'audio:.*', '', callback.message.caption)
    callback.message.caption = re.sub(r'user_id:.*', '', callback.message.caption)
    await callback.message.edit_caption(f'{callback.message.caption}\n--------------------\n❌ОТКЛОНЕНА❌', parse_mode='html')
    await bot.send_message(config['MODERS_CHAT'], f'@{callback.from_user.username}, напиши причину отказа.')
    await DeclinePostState.decline_reason.set()

@dp.message_handler(state=DeclinePostState.decline_reason)
async def get_decline_reason(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    if message.from_user.id == state_data['moder_id']:
        decline_reason = message.text
        await bot.send_message(state_data['declined_user_id'], f'К сожалению, твоя заявка отклонена, по причине:\n\n'
                                                               f'{decline_reason}')
        await state.finish()


# Callback ответа на report
@dp.callback_query_handler(lambda callback: callback.data == 'answer_to_report')
async def process_callback_answer_to_report(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(report_user_id=re.findall(r'user_id:.*', callback.message.text)[0].replace('user_id: ', '').replace('\n', ''))
    await state.update_data(moder_id=callback.from_user.id)
    await state.update_data(report=re.findall(r'ТЕКСТ:.*', callback.message.text)[0])
    await bot.send_message(config['MODERS_CHAT'], f'@{callback.from_user.username}, напиши ответ на report.')
    await ReportAnswerState.answer.set()
@dp.message_handler(state=ReportAnswerState.answer)
async def get_decline_reason(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    if message.from_user.id == state_data['moder_id']:
        report_answer = message.text
        await bot.send_message(state_data['report_user_id'], f'Пришел ответ на твоё обращение:\n\n'
                                                             f'❓ {state_data["report"]}\n\n'
                                                             f'❗ ОТВЕТ: {report_answer}\n\n')
        await state.finish()
