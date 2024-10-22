from lua_runner import runtime_strategy_interface as rsi
from lua_runner import lua_api

class LuaRuntime:
    '''
    Runtime strategy contextual class
    '''
    
    def __init__(self, strategy: rsi.RuntimeStrategyInterface):
        '''
        Runtime strategy contextual class
        
        Args:
            strategy: strategy to be used 
        '''
        
        self.strategy = strategy
        
    def execute(self, code: str) -> None:
        '''
        Executes code
        
        Args:
            code: code to be executed
            
        Returns:
            None
        '''
        
        self.strategy.execute(code)
        
    def register_api(self, api: lua_api.LuaApi) -> None:
        '''
        Registers all methods from the API
        
        Args:
            lua_api: LuaApi - api to register
            
        Returns:
            None
        '''
        
        self.strategy.register_api(api)
