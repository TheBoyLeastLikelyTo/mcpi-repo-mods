import minecraft
import block
import time

mc = minecraft.Minecraft.create()

mc.postToChat("hi, look up")

time.sleep(1)

pos = mc.player.getTilePos()

mc.setBlock(pos.x,pos.y+2,pos.z,block.DIAMOND_BLOCK)

mc.postToChat("now, look down")

time.sleep(1)

mc.setBlock(pos.x,pos.y-1,pos.z,block.DIAMOND_BLOCK)

mc.postToChat("try to jump!!")

time.sleep(1)

mc.postToChat("LOL")

time.sleep(1)

mc.postToChat("so long :D")
