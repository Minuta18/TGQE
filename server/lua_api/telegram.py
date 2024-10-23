import lua_runner

api = lua_runner.LuaApi('telegram')

class LuaMessage:
    '''
    Class that represents telegram message in Lua
    '''

    message_id: int|None = None    
    message_text: str|None = None
    image_path: str|None = None
    
    def __init__(self, 
        message_text: str|None = None, 
        image_path: str|None = None,
        message_id: int|None = None,
    ):
        '''
        Class that represents telegram message in Lua
        '''
        
        self.message_text = message_text
        self.image_path = image_path
        self.message_id = message_id
        
api.register_api_object('LuaMessage', LuaMessage)
