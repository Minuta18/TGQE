import logging
import os
from bot_main import TG_bot

logger = logging.getLogger('main')

logging.basicConfig(
    format='[%(levelname)s] %(asctime)s %(module)s.%(funcName)s: %(message)s', 
    level=logging.DEBUG
)

import lua_runner

def awesome_print(text):
    print('AWESOME PRINT:', text)

if __name__ == '__main__':
    api = lua_runner.LuaApi() # Class to handle LUA API
    # Registering function awesome_print in engine table, which will execute
    # awesome_print from python
    api.register_api_method('engine.awesome_print', awesome_print)
    
    # Class which will execute lua code
    cont = lua_runner.LuaRuntime(lua_runner.LupaStrategy())
    cont.register_api(api) # Allows lua to use methods from api 
    # Executes simple code:
    cont.execute('''
engine.awesome_print(\'Hello LUA!\')

function cool_sum(a, b) 
    return a + b
end
''')
    print(cont.call_func('cool_sum', args=(5, 3))) # Calls function from lua

    def request_to_server(message):
        return [['aboba', None]], [[None]]

    bot = TG_bot(token=os.environ.get('TOKEN'), request_to_server=request_to_server)
    bot.start()
