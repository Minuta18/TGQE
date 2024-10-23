import os
from bot_server.bot import TelegramBot

bot = TelegramBot(os.environ.get('TOKEN'))
