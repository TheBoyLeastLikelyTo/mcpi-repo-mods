import minecraft
import block

x = raw_input("what server ")

mc = minecraft.Minecraft.create(x, 4711)

while(True):
    event = mc.events.pollBlockHits()
    for event in event:
        epos = event.pos
        etype = event.type
        mc.setBlock(epos.x,epos.y,epos.z,block.TNT.id,1)
