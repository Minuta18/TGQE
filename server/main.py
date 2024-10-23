import logging
import os
from bot_main import TG_bot

logger = logging.getLogger('main')

logging.basicConfig(
    format='[%(levelname)s] %(asctime)s %(module)s.%(funcName)s: %(message)s', 
    level=logging.DEBUG
)

import lua_runner
import lua_api

if __name__ == '__main__':
    cont = lua_runner.LuaRuntime(lua_runner.LupaStrategy())
    cont.register_api(lua_api.engine_api)
    cont.execute('''
engine.utils.print_hello_world()
''')
    print(cont.call_func('cool_sum', args=(5, 3))) # Calls function from lua

    def request_to_server(message):
        return [['aboba', None]], [[None]]

    bot = TG_bot(token=os.environ.get('TOKEN'), request_to_server=request_to_server)
    bot.start()
