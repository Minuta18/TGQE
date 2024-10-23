import lua_runner
from lua_api import utils
from lua_api import telegram

engine_api = lua_runner.LuaApi('engine')
engine_api.include_api(utils.api)
engine_api.include_api(telegram.api)
