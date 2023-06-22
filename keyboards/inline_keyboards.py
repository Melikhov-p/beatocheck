from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Стартовая клавиатура
inline_enter_btn = InlineKeyboardButton('Меню', callback_data='menu_btn')
inline_enter_kb = InlineKeyboardMarkup()
inline_enter_kb.add(inline_enter_btn)

# Основное меню
menu_send_beat_btn = InlineKeyboardButton(f"🎵 Отправить Бит 🎵", callback_data='send_beat_btn')
menu_buy_beat_btn = InlineKeyboardButton(f"💵 Как купить Бит 💵", callback_data='buy_beat_btn')
menu_rules_btn = InlineKeyboardButton(f"📖 Правила 📖", callback_data='menu_rules_btn')
menu_report_btn = InlineKeyboardButton(f"❗ Возникли проблемы ❗", callback_data='menu_report_btn')
menu_info_btn = InlineKeyboardButton(f"❓ Справка ❓", callback_data='menu_info_btn')
inline_menu_kb = InlineKeyboardMarkup(row_width=1)
inline_menu_kb.add(menu_send_beat_btn, menu_buy_beat_btn, menu_rules_btn, menu_report_btn, menu_info_btn)

# Тест клавиатура
inline_btn_2 = InlineKeyboardButton('Вторая кнопка', callback_data='button2')
inline_btn_3 = InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd')  # заполнить поле ввода текста ответом боту с текстом switch_inline_query_current_chat
inline_btn_4 = InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty')
inline_kb2 = InlineKeyboardMarkup(row_width=1)
inline_kb2.add(inline_btn_2, inline_btn_3, inline_btn_4)
