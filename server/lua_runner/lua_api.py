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
        self._namespaces = dict()
        self._namespaces[''] = dict() # no namespace
        
    def register_api_method(
        self,
        lua_name: str, 
        py_method: typing.Callable[..., typing.any],
        namespace: str = '',
    ) -> None:
        '''
        Registers new API method
        
        Registers new API method which will be available as namespace.py_method
        in lua. If namespace is \'\', namespace is unused (namespace.py_method
        becomes py_method). If lua_name in current namespace is already used, raises 
        IndexError.
        
        Args:
            lua_name: str - function name in lua
            py_method: Callable - function in python
            namespace: str (optional) - name of namespace to store it
            
        Raises:
            IndexError - if lua_name in current namespace is already used
            
        Returns:
            None
        '''
        if self._namespaces.get(namespace) is not None:
            if self._namespaces[namespace].get(lua_name) is not None:
                raise IndexError(f'lua_name={lua_name} is already used')
            self._namespaces[namespace][lua_name] = py_method
            return
        self._namespaces = dict()
        self._namespaces[namespace][lua_name] = py_method
    
    def change_api_method(
        self,
        lua_name: str, 
        py_method: typing.Callable[..., typing.any],
        namespace: str = '',
    ) -> None:
        '''
        Changes API method
        
        Doing everything exactly same as `register_api_method`, but without 
        checks. 
        
        Args:
            lua_name: str - function name in lua
            py_method: Callable - function in python
            namespace: str (optional) - name of namespace to store it

        Returns:
            None
        '''
        
        if self._namespaces.get(namespace) is not None:
            self._namespaces[namespace][lua_name] = py_method
            return
        self._namespaces = dict()
        self._namespaces[namespace][lua_name] = py_method
        
    def get_all_methods(self) -> dict[
        str, dict[str, typing.Callable[..., typing.any]]
    ]:
        '''
        Returns all methods
        
        Returns all methods and represent as dict
        '''
        
        return self._namespaces
        