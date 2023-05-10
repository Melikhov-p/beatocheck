from aiogram import executor

from loader import dp
from utils.set_commands import set_default_commands
# Handlers
from handlers.users import callback_handlers, command_handlers
from handlers.admins_chat import admins_chat_callback_handlers, admins_chat_command_handlers
from handlers.admins import admins_commands_handlers

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
