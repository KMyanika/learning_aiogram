from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_bot_commands(bot: Bot):
    custom_commands = [
        BotCommand(command="start", description="Перезапуск бота, на стартовую позицию 🏁"),
        BotCommand(command="getmyid", description="Бот покажет ваш id пользователя Telegram 👾"),
        BotCommand(command="help", description="Команда для связи с админом о помощи"),
        BotCommand(command='homework', description='Получить домашнее задание')
    ]

    await bot.set_my_commands(
        commands=custom_commands, scope=BotCommandScopeAllPrivateChats()
    )