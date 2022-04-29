from vpython import *

def collisionEnemies(player, enemies):
    for enemy in enemies:
        if collisionEnemy(player, enemy):
            return True
    return False

def collisionEnemy(player, enemy):
    enemyRadius = 4
    if abs(player['pos'][0] - enemy['pos'][0]) > enemyRadius:
        return False

    if abs(player['pos'][1] - enemy['pos'][1]) > enemyRadius:
        return False

    print('its a contact')

    return True

def hitStart(player):
    if abs(player['pos'][0]) > 20:
        return False
    if abs(10-player['pos'][1]) > 5:
        return False

    return True