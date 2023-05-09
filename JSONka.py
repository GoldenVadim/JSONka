class InvalidValue():
    def __init__(self,*args:object) -> None:"""The exception."""
def __convert_value__(value):
    if value is str:return value
    if value==None:return'null'
    if value==True:return'true'
    elif value==False:return'false'
    else:raise InvalidValue('JSONka: Invalid value for the key.')
class JSON():
    '''
A JSON object.
'''
    def __init__(self) -> object:
        self.data=[]
        self.parsed=''
        return self.data
    def add_key(self,key:str,value:str|int|bool|None):
        '''Adds key with value to JSON.'''
        self.data.append([key,__convert_value__(value)])
    def change_key(self,key:str,new_value=str|int|bool|None):
        '''Changes the value in key in JSON.'''
        for i in self.data:
            if key==i[0]:i[1]=new_value
    def clear(self):
        '''Clears the JSON.'''
        self.data.clear()
    def parse(self)->dict:
        self.parsed='{'
        for i in self.data:self.parsed=self.parsed+f'{i[0]}:{i[1]},'
        self.parsed.removesuffix(',')
        self.parsed=self.parsed+'}'
        self.parsed=dict(self.parsed)
        return self.parsed
    def to_bytes(self,encoding='UTF-8')->bytes:
        '''Returns a converted to bytes JSON object.'''
        return bytes(f'{self.parsed}',encoding)
    def save_to_file(self,path:str):
        '''Writes JSON to file.'''
        with open(path,'wt') as f:
            f.write(self.parsed)
            f.close()