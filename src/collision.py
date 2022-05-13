def collisionEnemies(player, enemies):
    for enemy in enemies:
        if collisionEnemy(player, enemy):
            return True
    return False

def collisionEnemy(player, enemy):
    enemyRadius = 5
    if distanceBetweenSpheres(player, enemy) > enemyRadius:
        return False

    return True

def distanceBetweenSpheres(sphere1, sphere2):
    x = (sphere1['pos'][0] - sphere2['pos'][0])**2
    y = (sphere1['pos'][1] - sphere2['pos'][1])**2
    hypothenuse = (x+y)**0.5
    return hypothenuse
    
# checks if player hit the start text
def hitStart(player):
    if abs(player['pos'][0]) > 20:
        return False
    if abs(10-player['pos'][1]) > 5:
        return False

    return True