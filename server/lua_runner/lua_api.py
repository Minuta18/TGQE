import typing

class LuaApi:
    '''
    Lua API class
    
    Class for collecting information about API methods
    '''
    
    def __init__(self):
        '''
        Lua API class
    
        Class for collecting information about API methods
        '''
        self._methods = dict()
        
    def register_api_method(
        self,
        lua_name: str, 
        py_method: typing.Callable[..., typing.any],
    ) -> None:
        '''
        Registers new API method
        
        Registers new API method which will be available as py_method
        in lua. If lua_name in current namespace is already used, raises 
        IndexError.
        
        Args:
            lua_name: str - function name in lua
            py_method: Callable - function in python
            
        Raises:
            IndexError - if lua_name in current namespace is already used
            
        Returns:
            None
        '''
        if self._methods.get(lua_name) is not None:
            raise IndexError(f'lua_name={lua_name} is already used')
        self._methods[lua_name] = py_method
    
    def change_api_method(
        self,
        lua_name: str, 
        py_method: typing.Callable[..., typing.any],
    ) -> None:
        '''
        Changes API method
        
        Doing everything exactly same as `register_api_method`, but without 
        checks. 
        
        Args:
            lua_name: str - function name in lua
            py_method: Callable - function in python

        Returns:
            None
        '''

        self._methods[lua_name] = py_method
        
    def get_all_methods(self) -> dict[
        str, dict[str, typing.Callable[..., typing.any]]
    ]:
        '''
        Returns all methods
        
        Returns all methods and represent as dict
        '''
        
        return self._methods
        