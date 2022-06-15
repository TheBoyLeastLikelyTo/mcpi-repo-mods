import minecraft
import block
import time

mc = minecraft.Minecraft.create()

while(True):
    if raw_input("say s to SUPERJUMP ") == "s":
        pos = mc.player.getTilePos()
        mc.player.setPos(pos.x,pos.y+10,pos.z)
    else:
        print("I guess you don't want to SUPERJUMP :,(")
        break
