import typing

class LuaApi:
    '''
    Lua API class
    
    Class for collecting information about API methods
    '''
    
    def __init__(self, table: str = None):
        '''
        Lua API class
    
        Class for collecting information about API methods
        
        Args:
            table: str - table, where methods are stored
        '''
        
        self._table = table
        self._methods = dict()
        self._included_apis = list()
        
    def register_api_method(
        self,
        lua_name: str, 
        py_method: typing.Callable[..., typing.Any],
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
        if self._table is not None:
            lua_name = f'{self._table}.{lua_name}'
        if self._methods.get(lua_name) is not None:
            raise IndexError(f'lua_name={lua_name} is already used')
        self._methods[lua_name] = py_method
    
    def change_api_method(
        self,
        lua_name: str, 
        py_method: typing.Callable[..., typing.Any],
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

        if self._table is not None:
            lua_name = f'{self._table}.{lua_name}'
        self._methods[lua_name] = py_method
        
    def get_all_methods(self) -> dict[
        str, dict[str, typing.Callable[..., typing.Any]]
    ]:
        '''
        Returns all methods
        
        Returns all methods and represents it as dict
        '''
        
        methods_to_return = self._methods
        for api in self._included_apis:
            apis_methods = api.get_all_methods()
            apis_methods_reformated = dict()
            for method in apis_methods.keys():
                apis_methods_reformated[f'{self._table}.{method}'] = \
                    apis_methods[method]
            methods_to_return.update(apis_methods_reformated)
            
        return methods_to_return
        
    def get_table_name(self) -> str:
        '''
        Returns name of the table, where methods will be created
        
        Returns:
            Name of the table
        '''
        
        return self._table
    
    def set_table_name(self, new_table_name: str) -> None:
        '''
        Changes the name of the table, where methods will be created
        
        Args:
            new_table_name: str - new name of the table
        '''
                
        for method in self._methods.keys():
            new_name = method.removesuffix(self._table + '.')
            if new_table_name is not None:
                new_name = f'{new_table_name}.{new_name}'
            self._methods[new_name] = self._methods[method]
            self._methods.pop(method, None)
    
        self._table = new_table_name
    
    def include_api(self, api: typing.Self) -> None:
        '''
        Includes all methods from the given api to this.
        
        If current table is specified, then all methods from the `api` will be 
        included in this table. E. g.
        
        ```python
        self._table = 'nice_table'
        self._methods = {
            'nice_table.nice_method': some_method,
        }
        
        some_api._table = 'cool_table'
        some_api._methods = {
            'cool_table.cool_method': some_method2,
        }
        
        self.include_api(some_api)
        
        # Will become to this:
        
        self._table = 'nice_table'
        self._methods = {
            'nice_table.nice_method': some_method,
            'nice_table.cool_table.cool_method': some_method2,
        }
        ```
    
        Also it's important to note that methods will be included only in 
        `get_all_methods()` method. So it stores just a *pointer* to a api, not
        api itself.
        
        Args:
            api: LuaApi - api to include
            
        Returns:
            None
        '''
    
        self._included_apis.append(api)
        
    def api_method(
        self, 
        func: typing.Callable[..., typing.Any], 
        lua_name: str
    ) -> typing.Callable[..., typing.Any]:
        '''
        Api method decorator
        
        Decorator which will add function as lua method automatically. Can be 
        used as following:
        
        ```python
        @your_api.api_method('example_method')
        def example_method(a: int, b: int) -> int:
            return a + b
        ```
        
        Args:
            lua_name: str - name in lua (can be different)
        '''
        
        def wrapper(*args, **kwargs):
            self.register_api_method(lua_name, func)
            return func(*args, **kwargs)
        return wrapper

    