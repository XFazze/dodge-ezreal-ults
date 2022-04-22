from vpython import *
from copy import copy
import math
from random import uniform, randint

def calcEnemies(enemies, player):
    enemies = spawnEnemies(enemies, player)
    for enemy in enemies:
        enemy = enemyPos(enemy)
        if enemy == None:
            enemies.remove(enemy)
    return enemies

def enemyPos(enemy):
    resEnemy = []
    pos = enemy['pos']
    pos[0] = pos[0]+pos[3]
    pos[1] = pos[1]+pos[4]
    if abs(pos[0]) > 110 or abs(pos[1]) > 110:
        return None

    enemy['pos'] = pos
    enemy['visual'].pos.x = pos[0]
    enemy['visual'].pos.y = pos[1]
    
    return enemy

def spawnEnemies(enemies, player):
    print('ene',enemies)
    if len(enemies) < 5:
        side = randint(0,1)
        sp = randint(0,2)-1
        sp2 = randint(0, 2)-1
        if side == 1:
            pos = [sp2*110, sp*randint(30,70),0, sp2*-randint(1,10)/10, sp*-randint(1,10)/10]
        elif side == 0:
            pos = [sp*randint(30,70),sp2*110, 0,sp*-randint(1,10)/10,sp2*-randint(1,10)/10]


        enemies.append({
            'pos' : pos,
            'visual' : sphere(pos=vec(pos[0],pos[1],pos[2]), radius=2)
        })
        
    return enemies

def curvePosToVec(pos):
    vecPos = [vec(pos[0]+5,pos[1],pos[2]),
    vec(pos[0],pos[1]+5,pos[2]),
    vec(pos[0]-5,pos[1],pos[2])
    ]
    return vecPos