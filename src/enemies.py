from vpython import vec, sphere
from copy import copy
from random import randint

def calcEnemies(enemies, player, enemyAmount):
    enemies = spawnEnemies(enemies, player, enemyAmount)
    for i, enemy in enumerate(enemies):
        enemy = enemyPos(enemy)
        if enemy == None:
            del enemies[i]
    return enemies

def enemyPos(enemy):
    resEnemy = []
    pos = enemy['pos']
    pos[0] = pos[0]+pos[3]
    pos[1] = pos[1]+pos[4]
    if abs(pos[0]) > 140 or abs(pos[1]) > 120:
        return None

    enemy['pos'] = pos
    enemy['visual'].pos.x = pos[0]
    enemy['visual'].pos.y = pos[1]
    
    return enemy

def spawnEnemies(enemies, player, enemyAmount):
    if len(enemies) < enemyAmount:
        side = randint(0,1)
        sp = 1 if randint(0,1) == 0 else -1
        sp2 = 1 if randint(0,1) == 0 else -1
        if side == 1:
            pos = [sp2*130, sp*randint(30,70),0, sp2*-randint(1,10)/10, sp*-randint(1,10)/10]
        else:
            pos = [sp*randint(30,70),sp2*110, 0,sp*-randint(1,10)/10,sp2*-randint(1,10)/10]

        enemies.append({
            'pos' : pos,
            'visual' : sphere(pos=vec(pos[0],pos[1],pos[2]), radius=2, color=vec(1,0,0))
        })
        
    return enemies

def curvePosToVec(pos):
    vecPos = [vec(pos[0]+5,pos[1],pos[2]),
    vec(pos[0],pos[1]+5,pos[2]),
    vec(pos[0]-5,pos[1],pos[2])
    ]
    return vecPos