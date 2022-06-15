import minecraft
import block
import time

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

while(True):
    playerPos = mc.player.getPos()
    x = playerPos.x
    y = playerPos.y
    z = playerPos.z
    mc.setBlock(x,y-1,z,block.STONE)
    
