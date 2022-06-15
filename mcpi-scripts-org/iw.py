import minecraft
import block

x = raw_input("what server ")

mc = minecraft.Minecraft.create(x, 4711)



while(True):
    event = mc.events.pollBlockHits()
    for event in event:
        epos = event.pos
        mc.postToChat("hi")
        for counter2 in range(0, 100):
            for counter1 in range(0, 50):
                mc.setBlock(epos.x, epos.y+counter1, epos.z+counter2, block.GOLD_BLOCK.id)
