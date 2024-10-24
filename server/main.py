import logging
import dotenv

logger = logging.getLogger('main')

logging.basicConfig(
    format='[%(levelname)s] %(asctime)s %(module)s.%(funcName)s: %(message)s', 
    level=logging.DEBUG
)

dotenv.load_dotenv('./.env')

import os
import asyncio
import lua_runner
import lua_api
import bot_server

cont = lua_runner.LuaRuntime(lua_runner.LupaStrategy())
cont.register_api(lua_api.engine_api)

preload = [
    'code:main.lua'
]

code_store = lua_runner.CodeStore(preload=preload)
for file in preload:
    cont.execute(code_store.get_code(file))
    
def message_handler(msg: lua_api.telegram.LuaMessage):
    cont.call_func('on_send', (msg, ))
    
bot_server.bot.set_message_handler(message_handler)

if __name__ == '__main__':
    # asyncio.run(bot_server.bot.run())
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(bot_server.bot.run())
    finally:
        loop.close()
