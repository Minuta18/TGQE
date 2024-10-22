from lua_runner import lua_api
import typing 

class RuntimeStrategyInterface:
    def execute(self, code: str) -> None: raise NotImplemented
    def register_api(self, api: lua_api.LuaApi) -> None: raise NotImplemented
    def call_func(self, func_name: str, args: typing.Any) -> None: 
        raise NotImplemented 
