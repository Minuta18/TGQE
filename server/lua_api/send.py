import bot_server
import typing
import lua_runner
import asyncio

api = lua_runner.LuaApi('telegram')

@api.api_method('send')
def send(msg: typing.Any):
    loop = asyncio.get_event_loop()
    loop.create_task(bot_server.bot.send_message(msg))
