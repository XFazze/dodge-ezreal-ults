from vpython import sphere, text, vec,rate, scene
from .playerMovement import playerMovement
from .collision import hitStart

def setup():
    scene.width = 1000
    scene.height = 800
    scene.title = "Dodge Ezreal Ults"
    scene.range = 100
    scene.background = vec(0.1, 0.1, 0.1)
    player = sphere(pos=vec(1, 2, 1), radius=2)
    return player

def menuSetup(playerVisual, speed):
    playerVisual.pos.x=0
    playerVisual.pos.y=0
    player = {"pos": [0, 0, 0], "vel": [0, 0, 0], "acc": [0, 0, 0]}

    enemies = []
    startText = text(text='Start', pos=vec(-20,30,0), height=8)
    while True:
        rate(speed)
        player, playerVisual = playerMovement(player,playerVisual)
        if hitStart(player):
            startText.visible = False
            break
    return playerVisual, enemies, player


    return playerVisual,enemies,player

