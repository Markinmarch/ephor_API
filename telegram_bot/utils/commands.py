from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


from telegram_bot.settings.config import CHANNEL_ID


async def set_commands_for_users(bot: Bot):
    menu_commands = [
        BotCommand(
            command = 'delete_account',
            description = 'Удалить учётную запись'
        ),
        BotCommand(
            command = 'create_post',
            description = 'Создать запись на канале'
        ),
        BotCommand(
            command = 'my_posts',
            description = 'Список моих записей'
        )
    ]

    await bot.set_my_commands(
        commands = menu_commands,
        scope = BotCommandScopeDefault()
    )