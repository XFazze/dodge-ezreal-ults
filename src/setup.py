from vpython import *


# TODO create mid walls
def setup():
    scene.width = 1000
    scene.height = 800
    scene.title = "Dodge Ezreal Ults"
    scene.range = 100
    scene.background = vec(0.1, 0.1, 0.1)
    # mainBox = box(pos=vector(10, 10, 10), heigt=1000, width=1000)
    player = sphere(pos=vec(1, 2, 1), radius=2)
    return player
