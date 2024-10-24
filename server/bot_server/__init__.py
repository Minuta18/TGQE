import os
from bot_server.tgbot import TelegramBot

bot = TelegramBot(os.environ.get('TOKEN'))
