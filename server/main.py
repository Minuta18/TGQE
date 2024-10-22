import logging

logger = logging.getLogger('main')

logging.basicConfig(
    format='[%(levelname)s] %(asctime)s %(module)s.%(funcName)s: %(message)s', 
    level=logging.DEBUG
)

import lua_runner

def awesome_print(text):
    print('SUSSY PRINT:', text)

if __name__ == '__main__':
    api = lua_runner.LuaApi()
    api.register_api_method('engine.awesome_print', awesome_print)
    cont = lua_runner.LuaRuntime(lua_runner.LupaStrategy(1000))
    cont.register_api(api)
    cont.execute('''
print(math.floor(0.1))
engine.awesome_print(\'Hello LUA!\')
''')
