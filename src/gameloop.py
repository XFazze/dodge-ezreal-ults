from vpython import *
from ults import *
from collition import *
from time import time

def gameLoop(playerVisual,player, enemies, speed):
    startTime = time()
    slowdiff = 2
    #diffText = text(text=f'Enemies: {slowdiff}', pos=vec(-100,90,0), height=8)

    while True:
        rate(speed)
        player, playerVisual = playerMovement(player,playerVisual)
        diff = (round(time()-startTime)*2+5)
        #if slowdiff != diff:
            #print('wee')
            #slowdiff = diff
            #diffText.text = f'Enemies: {slowdiff}'
            


        enemies = calcEnemies(enemies, player, diff)
        if collisionEnemies(player,enemies):
            print('breaking')
            break
    print('died')
    score = round(10*(time()-startTime))/10
    scoreText = text(text=f'Score : {score}', pos=vec(-20,30,0), height=8)
    sleep(1)
    
    continueText = text(text='Press button', pos=vec(-20,-30,0), height=8)
    while True:
        rate(speed)
        k = keysdown()
        if len(k) > 0:
            continueText.visible = False
            
            scoreText.visible = False
            #continueText = text(text="hej",pos=vec(-20,30,0),height=8,color=vec(0,0,0))
            for enemy in enemies:
                enemy["visual"].visible = False

            break


    print('go next')
    #show dead


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