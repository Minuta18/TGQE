import asyncio
import aiogram
import typing
import logging

class TelegramBot:
    def __init__(self, token: str):
        self._dp = aiogram.Dispatcher()
        self._token = token
        self._bot = aiogram.Bot(
            self._token, 
            parse_mode=aiogram.enums.ParseMode.HTML
        ) 
        
    
        
    async def run(self):
        logging.info('Server started')
        await self._dp.start_polling(self._bot)   
    
        
