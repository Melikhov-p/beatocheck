from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot, config
from aiogram import types
import re
from states.AdminChatStates import DeclinePostState


# Callback's модерации поста


@dp.callback_query_handler(lambda callback: callback.data == 'admin_accept_post')
async def process_callback_accept_post_to_channel(callback: types.CallbackQuery):
    audio_id = re.findall(r'audio:.*', callback.message.caption)[0].replace('audio:', '')  # id файла с аудио из сообщения
    user_id = re.findall(r'user_id:.*', callback.message.caption)[0].replace('user_id:', '')
    callback.message.caption = re.sub(r'audio:.*', '', callback.message.caption)
    callback.message.caption = re.sub(r'user_id:.*', '', callback.message.caption)
    await callback.message.edit_caption(f'{callback.message.caption}\n\n--------------------\n✅ОДОБРЕНА✅', parse_mode='html')
    await bot.send_message(user_id, 'Твой бит одобрен к размещению, он уже в канале @beatocheck')  # Сообщение юзеру что бит одобрен
    await bot.send_photo(config['CHANNEL_ID'], photo=callback.message.photo[-1].file_id, caption=callback.message.caption.replace('@ ', '@'), parse_mode='html')
    await bot.send_audio(config['CHANNEL_ID'], audio=audio_id, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Пожаловаться', callback_data='report_for_post')))


@dp.callback_query_handler(lambda callback: callback.data == 'admin_decline_post')
async def process_callback_decline_post_to_channel(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(declined_user_id=re.findall(r'user_id:.*', callback.message.caption)[0].replace('user_id:', ''))
    callback.message.caption = re.sub(r'audio:.*', '', callback.message.caption)
    callback.message.caption = re.sub(r'user_id:.*', '', callback.message.caption)
    await callback.message.edit_caption(f'{callback.message.caption}\n\n--------------------\n❌ОТКЛОНЕНА❌', parse_mode='html')
    await bot.send_message(config['MODER_CHAT'], f'@{callback.from_user.username}, напиши причину отказа.')
    # await bot.send_message(config['MODER_CHAT'], f'@{callback.from_user.username}, не забудь написать причину отклонения заявки по шаблону:\n'
    #                                               f'/decline_reason user_id//причина')
    await DeclinePostState.decline_reason.set()

@dp.message_handler(state=DeclinePostState.decline_reason)
async def get_decline_reason(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    decline_reason = message.text
    await bot.send_message(state_data['declined_user_id'], f'К сожалению, твоя заявка отклонена, по причине:\n\n'
                                                           f'{decline_reason}')
    await state.finish()
