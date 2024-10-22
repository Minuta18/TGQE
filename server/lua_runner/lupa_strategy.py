import sys
import logging
import typing
from lua_runner import lua_api

logger = logging.getLogger('main')

try:
    import lupa.luajit21 as lupa
except ImportError:
    logger.critical('Unable to load LuaJIT 2.1. Exiting...')
    sys.exit(-1)
logger.info('LuaJIT 2.1 loaded successfully')

from lua_runner import runtime_strategy_interface as rsi

class LupaStrategy(rsi.RuntimeStrategyInterface):
    '''
    Lua runtime strategy that implements it using lupa library
    '''
    
    def __init__(self, max_memory: int = 1000):
        '''
        Lua runtime strategy that implements it using lupa library
        
        Args:
            max_memory: max memory which lua can allocate (Doesn't work now 
                cause there is no specify what this param means in lupa docs)
        '''
        
        self._runtime = lupa.LuaRuntime(unpack_returned_tuples = True)
        
    def _get_lua_object(self, 
        object: str, 
        raise_if_not_found: bool = True,
    ) -> typing.Any:
        namespaces = object.split('.')
        curr_namespace = self._runtime.globals()
        for namespace in namespaces[:-1]:
            if curr_namespace[namespace] is None:
                if raise_if_not_found:
                    raise IndexError('Can\'t find such object')
                curr_namespace[namespace] = self._runtime.eval('{}')
            curr_namespace = curr_namespace[namespace]
        return curr_namespace[namespaces[-1]]
        
    def _set_lua_object(self, 
        object: str, 
        value: typing.Any,
        raise_if_not_found: bool = True,
    ) -> None:
        namespaces = object.split('.') # Some code duplication cause I lazy
        curr_namespace = self._runtime.globals()
        for namespace in namespaces[:-1]:
            if curr_namespace[namespace] is None:
                if raise_if_not_found:
                    raise IndexError('Can\'t find such object')
                curr_namespace[namespace] = self._runtime.eval('{}')
            curr_namespace = curr_namespace[namespace]
        curr_namespace[namespaces[-1]] = value
        
    def execute(self, code: str) -> None:
        '''
        Executes code
        
        Args:
            code: code to be executed
            
        Returns:
            None
        '''
        
        self._runtime.execute(code)
        
    def register_api(self, lua_api: lua_api.LuaApi) -> None:
        '''
        Registers all methods from the API
        
        Args:
            lua_api: LuaApi - api to register
            
        Returns:
            None
        '''
        
        methods = lua_api.get_all_methods()
        
        for method in methods.keys():
            self._set_lua_object(method, methods[method], False)

    def call_func(self, func_name: str, args: typing.Any = ()) -> typing.Any:
        '''
        Calls function from lua
        
        Args:
            func_name: str - function name. table.func means call func from 
            table table.
            
        Returns:
            What function returns
        '''
        
        # TODO: Wouldn't it be better just to use lua.execute here? Need to 
        #       check in future...
        return self._get_lua_object(func_name, raise_if_not_found=True)(*args)
        