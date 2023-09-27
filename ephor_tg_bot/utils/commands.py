from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat


# from ephor_tg_bot.core.config import CHANNEL_ID
from ephor_tg_bot.core.config import ADMIN_IDS, BOT_URL


user_commands = [
    BotCommand(
        command = 'start',
        description = 'Авторизация'
    )
]

admin_commands = [
    BotCommand(
        command = 'start',
        description = 'Авторизация'
    ),
    BotCommand(
        command = 'create_task',
        description = 'Создать задание'
    )
]

async def set_commands(bot: Bot):
    await bot.set_my_commands(
        commands = user_commands,
        scope = BotCommandScopeDefault()
    )
    for admin in ADMIN_IDS:
        await bot.set_my_commands(
            commands = admin_commands,
            scope = BotCommandScopeChat(chat_id = admin)
        )