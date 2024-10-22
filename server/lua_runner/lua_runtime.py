from lua_runner import runtime_strategy_interface as rsi

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
