# CHARACTER MODULE

class Character:
    '''
    The base character class, serves as the mother class for specialized characters such as heroes and enemies.
    '''
    
    def __init__(self):
        
        self.HP = 0
        self.STR = 0
    
    
class Hero(Character):
    '''
    Child class of character. Has hero features in addition to basic attributes.
    '''
    
    def __init__(self):
        Character.__init__(self)
        

if __name__ == '__main__':
    pavel = Hero()