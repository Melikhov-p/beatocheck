from aiogram import executor

from loader import dp
from utils.set_commands import set_default_commands
# Handlers
from handlers.users import callback_handlers, command_handlers
from handlers.moders_chat import moders_chat_callback_handlers, moders_chat_command_handlers
from handlers.admins import admins_commands_handlers
from handlers.scripts import buy_beat_script, send_beat_script

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
