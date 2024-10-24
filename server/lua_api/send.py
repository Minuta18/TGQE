from bot_server import tgbot
import typing
import lua_runner

api = lua_runner.LuaApi('telegram')

@api.api_method('send')
def send(msg: typing.Any):
    tgbot.message_queue.append(msg)
    