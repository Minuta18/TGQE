import sys
import logging
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
            namespaces = method.split('.')
            curr_namespace = self._runtime.globals()
            for namespace in namespaces[:-1]:
                if curr_namespace[namespace] is None:
                    curr_namespace[namespace] = self._runtime.eval('{}')
                curr_namespace = curr_namespace[namespace]
            curr_namespace[namespaces[-1]] = methods[method]

