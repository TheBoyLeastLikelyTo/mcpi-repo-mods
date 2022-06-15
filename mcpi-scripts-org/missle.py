import minecraft
import block
import time
cs = raw_input("what server ")
mc = minecraft.Minecraft.create(cs, 4711)
pos = mc.player.getTilePos()  

xs = raw_input("enter the x pos where it should land ")
zs = raw_input("enter the y pos where it should land ")
yc = mc.getHeight(int(xs), int(zs))

x = 0
y = 0
g = 0
ys = 0

currentHeight = pos.y
print("Start Program: currentHeight is: " + str(currentHeight))
	
for ys in range(0, 70):
	print ("ys is " + str(ys))
	currentHeight = currentHeight + 1
	for x in range(currentHeight, currentHeight+20):
		print ("x is " + str(x))
        	mc.setBlock(pos.x+1,pos.y+x,pos.z, block.OBSIDIAN)
		y = y+1	
         	if y == 19:
        		mc.setBlock(pos.x+1,pos.y+currentHeight,pos.z, block.AIR)
			time.sleep(0.1)
			print("Current Height is: " + str(currentHeight))
			y = 0



mc.setBlocks(int(xs),50,int(zs), int(xs),61,int(zs), block.GRAVEL)
	
time.sleep(3)

mc.setBlocks(int(xs)+5, yc+5, int(zs)+5, int(xs)-5, yc-5, int(zs)-5, block.AIR)
mc.setBlocks(int(xs)+5, yc-5, int(zs)+5, int(xs)-5, yc-5, int(zs)-5,block.LAVA_FLOWING)
time.sleep(1)
mc.setBlocks(int(xs),yc-5,int(zs), int(xs),yc+8,int(zs), block.AIR)
time.sleep(0.5)
mc.setBlocks(int(xs),yc-5,int(zs), int(xs),yc+5,int(zs), block.OBSIDIAN)
time.sleep(1)
mc.setBlocks(int(xs),yc-5,int(zs), int(xs),yc+5,int(zs), block.TNT.id,1)
mc.setBlocks(int(xs),yc-5,int(zs), int(xs),yc+5,int(zs), block.AIR)
		

