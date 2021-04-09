#! /usr/bin/env python

import minecraft.minecraft as minecraft
import time
import minecraft.block as block
if __name__ == "__main__":

        time.sleep(2)
        mc = minecraft.Minecraft.create()
        mc.postToChat("Starting now!")
        time.sleep(1)
        playerPosition = mc.player.getPos()
        playerPosition = minecraft.Vec3(int(playerPosition.x), int(playerPosition.y), int(playerPosition.z))
        mc.setBlocks(playerPosition.x+1, playerPosition.y, playerPosition.z+1, playerPosition.x+9, playerPosition.y, playerPosition.z+9, block.COBBLESTONE)  
        mc.setBlocks(playerPosition.x+1, playerPosition.y+1, playerPosition.z+1, playerPosition.x+9, playerPosition.y+1, playerPosition.z+1, block.WOOD)
        mc.setBlocks(playerPosition.x+9, playerPosition.y+1, playerPosition.z+1, playerPosition.x+9, playerPosition.y+1, playerPosition.z+9, block.WOOD)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+1, playerPosition.z+9, playerPosition.x+1, playerPosition.y+1, playerPosition.z+1, block.WOOD)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+1, playerPosition.z+9, playerPosition.x+9, playerPosition.y+1, playerPosition.z+9, block.WOOD)
        time.sleep(3)
        mc.setBlock(playerPosition.x+1, playerPosition.y+1, playerPosition.z+5, block.AIR)
        mc.setBlock(playerPosition.x+0, playerPosition.y, playerPosition.z+5, block.STONE_SLAB)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+2, playerPosition.z+1, playerPosition.x+9, playerPosition.y+2, playerPosition.z+1, block.WOOD)
        mc.setBlocks(playerPosition.x+9, playerPosition.y+2, playerPosition.z+1, playerPosition.x+9, playerPosition.y+2, playerPosition.z+9, block.WOOD)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+2, playerPosition.z+9, playerPosition.x+1, playerPosition.y+2, playerPosition.z+1, block.WOOD)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+2, playerPosition.z+9, playerPosition.x+9, playerPosition.y+2, playerPosition.z+9, block.WOOD)
        time.sleep(3)
        mc.setBlock(playerPosition.x+1, playerPosition.y+2, playerPosition.z+5, block.AIR)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+4, playerPosition.z+1, playerPosition.x+9, playerPosition.y+4, playerPosition.z+9, block.GLOWSTONE_BLOCK)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+3, playerPosition.z+1, playerPosition.x+9, playerPosition.y+4, playerPosition.z+1, block.WOOD)
        mc.setBlocks(playerPosition.x+9, playerPosition.y+3, playerPosition.z+1, playerPosition.x+9, playerPosition.y+4, playerPosition.z+9, block.WOOD)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+3, playerPosition.z+9, playerPosition.x+1, playerPosition.y+4, playerPosition.z+1, block.WOOD)
        mc.setBlocks(playerPosition.x+1, playerPosition.y+3, playerPosition.z+9, playerPosition.x+9, playerPosition.y+4, playerPosition.z+9, block.WOOD)
        time.sleep(3)
        mc.setBlock(playerPosition.x+1, playerPosition.y+1, playerPosition.z+5, block.AIR)
        mc.setBlock(playerPosition.x+1, playerPosition.y+2, playerPosition.z+5, block.AIR)
        mc.setBlock(playerPosition.x+8, playerPosition.y+1, playerPosition.z+5, block.CRAFTING_TABLE)
        mc.setBlock(playerPosition.x+8, playerPosition.y+1, playerPosition.z+6, block.FURNACE_ACTIVE)
        mc.setBlock(playerPosition.x+8, playerPosition.y+1, playerPosition.z+4, block.FURNACE_ACTIVE)
        mc.setBlock(playerPosition.x+8, playerPosition.y+1, playerPosition.z+7, block.CHEST.id, 4)
        mc.setBlock(playerPosition.x+8, playerPosition.y+1, playerPosition.z+3, block.CHEST.id, 4)
        time.sleep(2)
        mc.player.setTilePos(playerPosition.x+4, playerPosition.y+1, playerPosition.z+5)
