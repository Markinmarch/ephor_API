from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from telegram_bot.settings.config import CHANNEL_ID

async def set_commands_for_new_user(bot: Bot):
    menu_commands = [
        BotCommand(
            command = 'create_account',
            description = 'Создать учётную запись'
        ),
        BotCommand(
            command = 'rules',
            description = 'Правила пользования телеграм-каналом'
        ),
        BotCommand(
            command = 'contact',
            description = 'Связь с администрацией канала'
        )         
    ]

    await bot.set_my_commands(
        commands = menu_commands,
        scope = BotCommandScopeDefault()
    )

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
        ),
        BotCommand(
            command = 'rules',
            description = 'Правила пользования телеграм-каналом'
        ),
        BotCommand(
            command = 'contact',
            description = 'Связь с администрацией канала'
        ),
        BotCommand(
            command = 'test',
            description = 'Команда для тестирования'
        )
    ]

    await bot.set_my_commands(
        commands = menu_commands,
        scope = BotCommandScopeDefault()
    )