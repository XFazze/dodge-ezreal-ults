from vpython import *
from time import sleep
from setup import *
from gameloop import *
from ults import *

playerVisual = setup()
speed  = 100
while True:
    playerVisual, enemies, player = menuSetup(playerVisual, speed)
    print('DONE WITH MENU')
    gameLoop(playerVisual, player, enemies, speed)



# gameloop
# move in arena
# acceleration and velocity
# check if hit wall

# random ez ults
# check collision

# score
