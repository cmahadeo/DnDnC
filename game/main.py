# MAIN

# IMPORT A BUNCH OF MODULES
import os, time, random

from libs import *


# THIS IS WHERE THE MAIN GAME LOOP OCCURS
# 3 PARTS:

# INITIALIZE
game = game.Game()

# Load a game from a folder

# GAME LOOP
done = False
while not done:
    com = input("Command: ")
    
    # game.event(com)
    # Print from game
    if com == 'CLOSE':
        done = True

# CLOSING LINES
