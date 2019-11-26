# WE WANT TO IMPORT MATH
# import math # <- MATH IS A MODULE

# from math import pi, cos # <- ONLY IMPORTS THE PI CONSTANT
# import math.pi as chrispi
# from math import pi, cos, tan

# Use from given you want to import multiple elements or submodules from same library
# Use import library.module if importing only one

# from math import * # * = EVERYTHING, generally NOT advised.

import os, random, time

if __name__ == '__main__':
    
    example = 2
    if example == 1:
        # OS FUNCTIONS
        dir_main = os.getcwd() # Returns the path of the running .py's folder, (i.e. current directory)
        dir_folder = os.path.join(dir_main, "chris_folder")
        dir_file = os.path.join(dir_main, "Lesson5.py")
        # This is equal to writing dir_folder = dir_main + '\\' + 'chris_folder'
        
        print(os.path.exists(dir_file))
        
        # CREATE FOLDER
        if not os.path.exists(dir_folder):
            os.mkdir(dir_folder) # <- Make directory (gives an error if the directory already exists)
        
        # LIST ALL FILES IN THE DIRECTORY
        dir_list = os.listdir(dir_main)
    
    
    
    
    
    
    # MORE RANDOMNESS!
    a = int(time.time()*100000) % 100 # Time at which the line is run (the nanosecond)
    random.seed(a=a)
    
    # Return certain random values
    dice_roll = random.randint(1, 6) # Returns a random integer on [1,6], D6
    
    L = ['hero1', 'hero2', 'hero3']
    selection = random.choice(L) # Returns a random element from list L
    
    sel_list = random.sample(range(10), 4) # Returns a random sublist of 3 elements from range(10) (list from 0 to 9), (without replacement)
    rand_L = random.sample(L, 2)
    
    # WITH REPLACEMENT
    dice_rolls = [random.randint(1,8) for k in range(4)] # Gives a list of 4 D8 rolls
    
    # ABOVE IS EQUIVALENT TO:
    dice_rolls2 = []
    for j in range(4):
        dice_rolls2.append(random.randint(1,8))
    
    print(a, selection)