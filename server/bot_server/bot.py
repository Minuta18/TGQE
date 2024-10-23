import asyncio
import aiogram
import typing
import logging

import lua_api

class TelegramBot:
    def __init__(self, token: str):
        self._dp = aiogram.Dispatcher()
        self._token = token
        self._bot = aiogram.Bot(
            self._token, 
            parse_mode=aiogram.enums.ParseMode.HTML
        ) 
        
        @self._dp.message()
        async def message_handler(self, message: aiogram.types.Message):
            pass
        
    async def send_message(
        chat_id: int, 
        msg: lua_api.telegram.LuaMessage
    ) -> None:
        if msg.image_path is None:
            if msg.message_text is None:
                raise ValueError(
                    'Either image_path or message_text must be specified'
                )
            await aiogram.methods.send_photo.SendPhoto(
                chat_id=chat_id,
                photo=aiogram.types.FSInputFile(
                    path=msg.image_path,
                    filename=msg.image_filename,
                ),
                caption=msg.message_text,
                show_caption_above_media=(msg.message_text is not None)
            )
            return
        await aiogram.methods.send_message.SendMessage(
            chat_id=chat_id,
            text=msg.message_text
        )
        
    async def run(self):
        logging.info('Server started')
        await self._dp.start_polling(self._bot)   
    
        
