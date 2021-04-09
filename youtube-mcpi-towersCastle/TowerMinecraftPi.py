from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlocks(x + 2, y + 10, z + 2, x - 2,y - 2, z - 2, STONE_BRICK.id)
mc.setBlocks(x + 1, y + 10, z + 1, x - 1,y - 1, z - 1, AIR.id)
mc.setBlocks(x + 2, y + 9, z + 2, x - 2,y + 9, z - 2, MOSS_STONE.id)
mc.setBlock(x + 1, y + 9, z + 1, AIR.id)

