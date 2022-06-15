import minecraft
import block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

up = pos.y

forw = pos.x

z = pos.z

length = 1000

mc.postToChat("stairway, to MELON!!!")

for x in xrange(0, length):
    forw = forw+1
    mc.setBlock(forw,up,z,block.MELON)
    up = up + 1
