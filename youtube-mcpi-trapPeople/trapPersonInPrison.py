x,y,z = -59,27,-22 #my prison coordinates, change that to yours
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
print(mc.getPlayerEntityIds())
choice = int(input('which one?'))
mc.entity.setTilePos(choice,(x,y,z))
mc.setting('world_immutable',True)
print('done')
