# GAME MODULE

class Game:
    '''
    The main class that contains all elements of the DnD session. Includes lists of heroes, enemies, items, NPCs, etc,
    and the management methods such as 'load', 'save', etc.
    '''
    
    def __init__(self):
        self.mode = 'explore'
        self.directory = ''
        
    
    def load(self, directory):
        '''
        Loads all game elements from the folder directory.
        '''
        
        pass
    
    
    def save(self, directory):
        '''
        Saves the game onto the directory.
        '''
        
        pass
    

if __name__ == '__main__':
    
    # DEBUG REGION
    game = Game()
    