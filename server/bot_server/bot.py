import aiogram
import logging
import typing

import lua_api

def _tg_bot_empty_callback(msg: lua_api.telegram.LuaMessage):
    return None

class TelegramBot:
    def __init__(self, token: str, on_send_callback: typing.Callable[
        [lua_api.telegram.LuaMessage], None 
    ] = _tg_bot_empty_callback):
        self._dp = aiogram.Dispatcher()
        self._token = token
        self._bot = aiogram.Bot(
            self._token, 
        ) 
        self._message_handler = on_send_callback
        
        @self._dp.message()
        async def message_handler(message: aiogram.types.Message):
            lua_message = lua_api.telegram.LuaMessage(
                message_text=message.md_text,
                message_id=message.message_id,
                chat_id=message.from_user.id
            )
            
            self._message_handler(lua_message)
        
    async def send_message(self,
        msg: lua_api.telegram.LuaMessage
    ) -> None:
        if msg.image_path is not None:
            if msg.message_text is None:
                raise ValueError(
                    'Either image_path or message_text must be specified'
                )
            await self._bot.send_photo(
                chat_id=msg.chat_id,
                photo=aiogram.types.FSInputFile(
                    path=msg.image_path,
                    filename=msg.image_filename,
                ),
                caption=msg.message_text,
                show_caption_above_media=(msg.message_text is not None)
            )
            return
        await self._bot.send_message(
            chat_id=msg.chat_id,
            text=msg.message_text
        )
        
    def set_message_handler(self, handler: typing.Callable[
        [lua_api.telegram.LuaMessage], None 
    ]):
        self._message_handler = handler
        
    async def run(self):
        logging.info('Server started')
        await self._dp.start_polling(self._bot)       
