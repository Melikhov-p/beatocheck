from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура отмены действия
cancel_btn = KeyboardButton('/cancel')
cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_kb.add(cancel_btn)  # Клавиатура
