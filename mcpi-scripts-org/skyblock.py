import minecraft
import block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

mc.postToChat("making skyblock...")

mc.setBlocks(pos.x+200,pos.y+200,pos.z+200,pos.x-200,pos.y-200,pos.z-200,block.AIR)

mc.setBlocks(pos.x+4,pos.y-1,pos.z+4,pos.x-4,pos.y-4,pos.z-4,block.GRASS)

mc.setBlock(pos.x,pos.y,pos.z,block.CHEST)

mc.setBlock(pos.x+1,pos.y,pos.z,block.SAPLING)
