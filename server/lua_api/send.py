from bot_server import tgbot
import bot_server
import typing
import lua_runner
import asyncio

api = lua_runner.LuaApi('telegram')

@api.api_method('send')
def send(msg: typing.Any):
    bot_server.tgbot.message_queue.put_nowait(msg)
    