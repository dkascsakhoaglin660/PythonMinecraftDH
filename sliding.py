from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

mc.player.getTilePos()
x, y, z = (mc.player.getTilePos)

while True:
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-0.2, 0.2)
    y = mc.getHeight(x,y)
    
    mc.player.setPos(x, y, z)
    time.sleep(0.1)