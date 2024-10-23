import os

class CodeStore:
    '''
    Class to store code
    '''
    
    _store: dict[str, str]
    
    def __init__(self, preload: list = []):
        '''
        Class to store code
        '''
        
        self._store = dict()
        
        for file in preload:
            self.get_code(file)
        
    def get_code(self, filename: str) -> str:
        '''
        Returns contents of text file. Caching it in self._store
        
        Args:
            filename: str - the ✨ filename ✨ 
        
        Returns:
            file contents
        '''
        
        if filename.startswith('code:'):
            filename = filename.removeprefix('code:')
            filename = os.path.join('../scripts/', filename)
        if self._store.get(filename) is not None:
            return self._store[filename]
        with open(filename, 'r') as file:
            self._store[filename] = file.read()
        return self._store[filename]
    