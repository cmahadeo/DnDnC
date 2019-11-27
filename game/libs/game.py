# GAME MODULE

class Game:
    '''
    The main class that contains all elements of the DnD session. Includes lists of heroes, enemies, items, NPCs, etc,
    and the management methods such as 'load', 'save', etc.
    '''
    
    def __init__(self):
        self.directory = ''
        self.mode = 'explore'
        
        # ELEMENTS
        self.heroes = {}
        self.npcs = {}
        self.enemies = {}
        
        self.location = 'None'
        
        
    # COMMANDS
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
    
    
    def show(self, *args):
        '''
        Prints a desired attribute.
        '''
        
        s = ''
        if len(args) == 0:
            s = 'Invalid input!'
        
        # Check the heroes, enemies, npc list
        
        return s
    
    
    def script(self, *args):
        '''
        Prints a desired script.
        '''
        
        pass
    
    
if __name__ == '__main__':
    
    # DEBUG REGION
    game = Game()

    