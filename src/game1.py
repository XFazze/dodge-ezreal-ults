from vpython import *
from time import sleep
from setup import *
from gameloop import *
from ults import *

playerVisual = setup()
enemies = []
player = {"pos": [0, 0, 0], "vel": [0, 0, 0], "acc": [1, 0, 0]}
keys = ""
speed  = 100
while True:
    rate(speed)
    player = calulatePlayerAcc(player)
    player = calulatePlayerVel(player)
    player = calulatePlayerPos(player)
    playerVisual.pos.x = player['pos'][0]
    playerVisual.pos.y = player['pos'][1]
    playerVisual.pos.z = player['pos'][2]
    enemies = calcEnemies(enemies, player)
    print(enemies)
    #print(player)


# gameloop
# move in arena
# acceleration and velocity
# check if hit wall

# random ez ults
# check collition

# score
