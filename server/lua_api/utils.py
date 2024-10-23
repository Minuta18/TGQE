import lua_runner

api = lua_runner.LuaApi('utils')

@api.api_method('print_hello_world')
def print_hello_world():
    print('Hello, world!!!')
