from vpython import *

def calcEnemies(enemies, player):
    enemies = spawnEnemies(enemies, player)
    for enemy in enemies:
        enemy = enemyPos(enemy)
    return enemies

def enemyPos(enemy):
    resEnemy = []
    pos = enemy[0]
    return enemy

def spawnEnemies(enemies, player):
    if len(enemies) == 0:
        enemies.append({
            'pos' : [0,0,0],
            'visual' : curve(pos=vec(pos[0], pos[1], pos[2]), radius=2)
        })
        
    return enemies