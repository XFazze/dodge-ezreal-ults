from vpython import rate, text, vec, keysdown
from time import time, sleep
from .enemies import calcEnemies
from .collision import collisionEnemies, hitStart 
from .setup import setup, menuSetup
from .playerMovement import playerMovement

def runGame():
    playerVisual = setup()
    speed  = 100
    while True:
        playerVisual, enemies, player = menuSetup(playerVisual, speed)
        gameLoop(playerVisual, player, enemies, speed)


def gameLoop(playerVisual,player, enemies, speed):
    startTime = time()

    while True:
        rate(speed)
        player, playerVisual = playerMovement(player,playerVisual)
        enemyAmount = (round(time()-startTime)*2+5)
        enemies = calcEnemies(enemies, player, enemyAmount)
        if collisionEnemies(player,enemies):
            break
    score = round(10*(time()-startTime))/10
    scoreText = text(text=f'Score : {score}', pos=vec(-20,30,0), height=8)
    sleep(1)

    playAgain(speed,scoreText, enemies)
    
    

def playAgain(speed,scoreText, enemies):
    continueText = text(text='Press button to continue', pos=vec(-40,-30,0), height=8)
    while True:
        rate(speed)
        k = keysdown()
        if len(k) > 0:
            continueText.visible = False
            scoreText.visible = False
            for enemy in enemies:
                enemy["visual"].visible = False

            break
