import logging

logger = logging.getLogger('main')

logging.basicConfig(
    format='[%(levelname)s] %(asctime)s %(module)s.%(funcName)s: %(message)s', 
    level=logging.DEBUG
)

import os
import lua_runner
import lua_api
import bot_server

if __name__ == '__main__':
#     cont = lua_runner.LuaRuntime(lua_runner.LupaStrategy())
#     cont.register_api(lua_api.engine_api)
#     cont.execute('''
# engine.utils.print_hello_world()
# ''')
#     print(cont.call_func('cool_sum', args=(5, 3))) # Calls function from lua
    bot = bot_server.TelegramBot(os.environ.get('TOKEN'))
    bot.run()
