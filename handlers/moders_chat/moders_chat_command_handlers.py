from aiogram import types

from loader import dp, bot, config


# Команды доступные только внутри админ чата
@dp.message_handler(chat_id=config['MODERS_CHAT'], commands=['decline_reason'])
async def process_send_decline_reason(message: types.Message):
    # args = message.get_args().split('//')
    # await bot.send_message(args[0], f'К сожалению, твоя заявка отклонена, по причине:\n\n'
    #                                 f'{args[1]}')
    await bot.send_message(config['MODERS_CHAT'], f'@{message.from_user.username}, эта команда в данный момент недоступна.')
