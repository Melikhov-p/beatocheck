import os
from aiogram.dispatcher import FSMContext
from loader import dp, bot, config
from aiogram import types
from states.BasicStates import BeatState
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.reply_keyboards import cancel_kb
from keyboards.admin_chat_keyboards import accept_post_btn, decline_post_btn

# --- СЦЕНАРИЙ ДОБАВЛЕНИЯ БИТА В КАНАЛ ---
@dp.callback_query_handler(lambda c: c.data == 'send_beat_btn')  # отправка бита в канал
async def get_beat_author(callback: types.CallbackQuery):  # callback знает из какого сообщения вызван, его текст и клавиатуру
    await bot.send_message(callback.from_user.id, "📪Чтобы отправить бит на витрину канала напиши сначала <b>свой псевдоним</b>:\n\n\n", parse_mode='html', reply_markup=cancel_kb)
    await BeatState.author.set()  # установка состояния указания автора бита, сохранение только в следующей ф-ии


@dp.message_handler(state=BeatState.author)  # хэндлер после автора
async def get_beat_title(message: types.Message, state: FSMContext):
    await state.update_data(author=message.text)  # Сохраняем данные память
    await bot.send_message(message.from_user.id, 'Теперь <b>название</b>', parse_mode='html')
    await BeatState.title.set()  # название бита


@dp.message_handler(state=BeatState.title)
async def get_beat_tags(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await bot.send_message(message.from_user.id, 'Теперь максимум 5 <b>тэгов</b>, разделённые пробелом.\n'
                                                 'Например: #Rap #Trap', parse_mode='html')
    await BeatState.tags.set()


@dp.message_handler(state=BeatState.tags)
async def get_beat_price(message: types.Message, state: FSMContext):
    tags = message.text.split(' ')
    if len(tags) <= 5:
        await state.update_data(tags=' '.join(tags))
        await bot.send_message(message.from_user.id, 'Теперь <b>обложку</b>', parse_mode='html')
        await BeatState.cover.set()
    else:
        await bot.send_message(message.from_user.id, f'Слишком много тегов ({len(tags)}), должно быть <b>не больше 5</b>.', parse_mode='html')
        await BeatState.tags.set()

@dp.message_handler(state=BeatState.cover, content_types=['photo'])
async def get_beat_cover(message: types.Message, state: FSMContext):
    await state.update_data(cover=message.photo[-1].file_id)
    await bot.send_message(message.from_user.id, 'Теперь <b>аудио-файл с <u>тегами автора</u></b>', parse_mode='html')
    await BeatState.tagged_beat.set()
@dp.message_handler(state=BeatState.cover, content_types=['text'])  # если получили не фото
async def process_cancel_command(message: types.Message):
    await message.answer('Отправь именно изображение, если хочешь прекратить отправь /cancel')


@dp.message_handler(state=BeatState.tagged_beat, content_types=['audio'])
async def get_beat_tagged_beat(message: types.Message, state: FSMContext):
    await state.update_data(tagged_beat=message.audio.file_id)
    await bot.send_message(message.from_user.id, 'И наконец <b>цену</b>', parse_mode='html')
    await BeatState.price.set()
@dp.message_handler(state=BeatState.tagged_beat, content_types=['text'])  # если получили не фото
async def process_cancel_command(message: types.Message):
    await message.answer('Отправь именно аудио файл, если хочешь прекратить отправь /cancel')


@dp.message_handler(state=BeatState.price)
async def get_beat_info_confirm(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    beat_data = await state.get_data()
    await bot.send_message(message.from_user.id, f"Проверим... 👀")
    await bot.send_photo(message.from_user.id, photo=beat_data['cover'], caption=f"""
<b>{beat_data['author']} - {beat_data['title']}</b>

<i>{beat_data['tags']}</i>

Цена: <b>{beat_data["price"]} ₽</b>
     """, parse_mode='html')  # reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'{beat_data["price"]}', callback_data='price_btn'))
    await bot.send_audio(message.from_user.id, audio=beat_data['tagged_beat'])
    await BeatState.confirm.set()
    await bot.send_message(message.from_user.id, 'Все верно?', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Да', callback_data='beat_info_confirm_yes'), InlineKeyboardButton('Нет', callback_data='beat_info_confirm_no')))


@dp.callback_query_handler(lambda c: c.data == 'beat_info_confirm_yes', state=BeatState.confirm)  # Информация по биту подтверждена | отправляем в админ чат на модерацию
async def process_send_beat_in_channel(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(confirm=callback.data)
    beat_data = await state.get_data()
    await bot.send_message(config['MODER_CHAT'], f'🔥🔥🔥Новая заявка на пост🔥🔥🔥\n\n'
                                                  f'От: {callback.from_user.username} ({callback.from_user.id})\n')  # Отправка поста в админ канал на модерацию
    await bot.send_audio(config['MODER_CHAT'], audio=beat_data['tagged_beat'])
    await bot.send_photo(config['MODER_CHAT'], photo=beat_data['cover'], caption=f"""
<b>{beat_data['author']} - {beat_data['title']}</b>

<i>{beat_data['tags']}</i>

Цена: <b>{beat_data["price"]} ₽</b> | Автор: @ {callback.from_user.username}
audio:{beat_data['tagged_beat']}
user_id:{callback.from_user.id}
         """, parse_mode='html', reply_markup=InlineKeyboardMarkup().add(accept_post_btn, decline_post_btn))  # Клавиатура модерации в админ чате, admins_chat_callback_handlers
    await bot.send_message(callback.from_user.id, f'<b>{beat_data["author"]} - {beat_data["title"]}</b> отправлен на модерацию, как только его одобрят, он появится на витрине @beatocheck', parse_mode='html')
    await state.finish()
    await callback.message.delete()
    # await process_callback_menu_btn(callback)


@dp.callback_query_handler(lambda c: c.data == 'beat_info_confirm_no', state=BeatState.confirm)  # Если окончательную инфу о бите не подтвердили
async def process_decline_send_beat_in_channel(callback: types.CallbackQuery, state: FSMContext):
    beat_data = await state.get_data()
    os.remove(beat_data['cover'])
    await bot.send_message(callback.from_user.id, f'Ладно, давай попробуем заново.', parse_mode='html')
    await state.finish()
    await get_beat_author(callback)
# --- КОНЕЦ СЦЕНАРИЯ ДОБАВЛЕНИЯ БИТА В КАНАЛ ---
