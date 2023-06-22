from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура модерации поста
accept_post_btn = InlineKeyboardButton('Принять', callback_data='admin_accept_post')
decline_post_btn = InlineKeyboardButton('Отклонить', callback_data='admin_decline_post')
admins_moderate_kb = InlineKeyboardMarkup()
admins_moderate_kb.add(accept_post_btn, decline_post_btn)
