import asyncio
import typing

import aiogram.methods.send_message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message


class TG_bot:
    def __init__(self, token: str, request_to_server: typing.Callable):
        self.dp = Dispatcher()
        self.token = token
        self.request_to_server = request_to_server

    def start(self):
        @self.dp.message()
        async def common_handler(message: Message):
            messages, buttons = self.request_to_server(message)

            builder = ReplyKeyboardBuilder()
            for button in buttons:
                builder.button(text=button)

            final_message = messages.pop(-1)

            for i in messages:
                if i[1] == None:
                    await aiogram.methods.send_message.SendMessage(chat_id=message.from_user.id, text=i[0])
                else:
                    await aiogram.methods.send_photo.SendPhoto(
                        chat_id=message.from_user.id,
                        photo=types.FSInputFile(path=i[1]),
                        caption=i[0],
                        show_caption_above_media=True
                    )

            if final_message[1] == None:
                await aiogram.methods.send_message.SendMessage(
                    chat_id=message.from_user.id,
                    text=final_message[0],
                    reply_markup=builder.as_markup(resize_keyboard=True)
                )
            else:
                await aiogram.methods.send_photo.SendPhoto(
                    chat_id=message.from_user.id,
                    photo=types.FSInputFile(path=final_message[1]),
                    captiom=final_message[0],
                    show_caption_above_media=True,
                    reply_markup=builder.as_markup(resize_keyboard=True)
                )

        async def start_bot():
            self.bot = Bot(self.token, parse_mode=ParseMode.HTML)
            await self.dp.start_polling(self.bot)

        asyncio.run(start_bot())