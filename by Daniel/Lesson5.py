# CLASSES AND METHODS!

# MUTABLE CLASS:
# DICT
# LIST
# STRING

# CUSTOM CLASS

# DRAGON MAID CLASS
# when naming classes, no underscore allowed and capitalize each separate word
class DragonMaid:
    '''
    A dragon maid object, with dragon maid attributes and methods!
    '''
    
    def __init__(self, name_string):
        '''
        Input your dragon maid attributes here. name_string is the name of your dragon maid!
        '''
        
        # DEFINE YOUR SET OF ATTRIBUTES FOR YOUR CUSTOM CLASS!
        self.name = name_string
        self.age = -1
        self.hobbies = [] # Default type = Actual type you want!
        self.breast_size = 0
    
    
    # Custom methods
    def speak(self):
        string = self.name + " says Daisuki!"
        print(string)
    
    
    def eat(self, food):
        '''
        Print the food our dragon maid ate.
        '''
        
        string = self.name + " ate a(n) " + food + "!"
        print(string)
        
    
    def test():
        '''
        Test. Call using DragonMaid.test()
        '''
        print("This is a test function!")
        
    
# INHERITANCE: Involves a parent class, and a child class

class Kanna(DragonMaid):
    '''
    This is a specific dragon maid class, for our dragon maid named Kanna!
    '''
    
    def __init__(self):
        
        # Inheritance initialization
        # This says: Initialize the DragonMaid class, when initializing the Kanna class, and store
        # all attributes from the DragonMaid initialization into our Kanna object (self)!
        DragonMaid.__init__(self, "Kanna")
        
        # LOLI SPECIFIC ATTRIBUTES
        self.preschool = 'Noname elementary school'
        self.friends = ["Tohru"]
        self.parent = "Kobayashi"
        
        # Current form
        self.form = "human"
    
    
    def transform(self):
        self.form = "dragon"
        print("Kanna is now in dragon form!")
        

# THE BIG QUESTION: When do we use classes, and when do we use dictionaries!

# Answer: Use dictionaries if you want to store information, and not change much.
# Use classes for when you want to constantly update your information structure.


# HERE IS A SNEAK PREVIEW OF DND!
class Game:
    '''
    This is our main game class. This is the game engine, where all the game computation will take place!
    '''
    
    def __init__(self):
        
        self.heroes = ["Pavel"]
        self.enemies = ["Spear Gnoll", "Boss Gnoll", "Knifey Bois"]
        self.setting = "Cave"
        
        self.inventory = ["Almost dead guy"]
        
    
    def load(self, folder):
        '''
        Load all elements from save folder.
        '''
        
        pass
    
    
    def save(self, folder):
        '''
        Save all elements onto a designated save folder.
        '''
        
        pass
    
    
    def input(self):
        '''
        Accept a user input as a command.
        '''
        
        pass
    

class Character:
    '''
    A basic character class holding the essential attributes that apply to every person or creature in the game.
    '''
    
    def __init__(self):
        
        self.health = 0
        self.mana = 0
        self.status = "Inactive"
        
        self.weapon = "None"
        self.abilities = []
        self.inventory = []
    
    
    def roll(self, sides):
        '''
        Sides is the dice type (6, 8, 10, 20). Roll a dice, and return the result.
        '''
        
        pass


class Hero(Character):
    '''
    A hero class.
    '''
    
    def __init__(self):
        
        Character.__init__(self)
        
        self.strength = 0
        self.agility = 0
        self.intellect = 0
        self.wisdom = 0
        self.charisma = 0
    
    
    def show_attr(self, attr):
        '''
        Prints the list of main attributes.
        '''
        
        if hasattr(self, attr):
            print(attr + " : " + str(getattr(self, attr)))
        

def ult(self, target):
    if target.status == 'invulnerable':
        return None
    elif target.health < 0.2*target.max_health:
        target.execute()
    
    
if __name__ == '__main__':
    
    # Initialized the list class as the object [1,2,3]
    # Assigning list to L
    L = [1,2,3]
    
    # FUNCTIONS
    # def f(x):
    
    # METHODS
    # x.method()
    # L.append(1), NOT append(L, 1)
    
    # INITIALIZE
    tohru = DragonMaid('Tohru')
    
    # INHERITANCE
    maid = Kanna()
    
