from  vpython import keysdown
def calulatePlayerAcc(player):
    keyAcc = [0,0,0]
    k = keysdown()
    speedAcc = 0.1
    if 'd' in k:
        keyAcc[0] = 1*speedAcc
    if 'a' in k:
        keyAcc[0] = -1*speedAcc
    if 'w' in k:
        keyAcc[1] = 1*speedAcc
    if 's' in k:
        keyAcc[1] = -1*speedAcc
    player['acc'] = keyAcc
    return player

def calulatePlayerVel(player):
    resVel = [0, 0, 0]
    for i, vel in enumerate(player["vel"]):
        if (vel + player["acc"][i]) != 0:
            negative = (vel + player["acc"][i])/abs((vel + player["acc"][i]))
        else:
            negative = 0
        if (vel + player["acc"][i])*0.99:
            resVel[i] = 0
        resVel[i] = (vel + player["acc"][i])*0.99 - 0.01*negative
    maxSpeed = 0.6
    if resVel[0] > maxSpeed: resVel[0] = maxSpeed
    if resVel[1] > maxSpeed: resVel[1] = maxSpeed
    if resVel[0] < -maxSpeed: resVel[0] = -maxSpeed
    if resVel[1] < -maxSpeed: resVel[1] = -maxSpeed
    player["vel"] = resVel
    #print(resVel)
    return player

def calulatePlayerPos(player):
    resPos = [0, 0, 0]
    for i, pos in enumerate(player["pos"]):
        resPos[i] = pos + player["vel"][i]
    if resPos[0] < -109 :resPos[0] = -109
    if resPos[0] > 109 :resPos[0] = 109
    if resPos[1] < -90 :resPos[1] = -90
    if resPos[1] > 90 :resPos[1] = 90
    player["pos"] = resPos
    #print(resPos)
    return player

def playerMovement(player,playerVisual):
    player = calulatePlayerAcc(player)
    player = calulatePlayerVel(player)
    player = calulatePlayerPos(player)
    playerVisual.pos.x = player['pos'][0]
    playerVisual.pos.y = player['pos'][1]
    playerVisual.pos.z = player['pos'][2]
    return player,playerVisual