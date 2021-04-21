# Imports
from mcpi import minecraft
from time import sleep

# The first input proccess
def MagicBearFIP():
    mc = minecraft.Minecraft.create()
    print("ʕ•ᴥ•ʔっ <(Some basic spots):\n\t• Spawn = 0.5, 0.0, 0.7\n\t• The Sky = 0.5, 100, 0.7")
    while True:
        try:
            x = float(input("ʕ•ᴥ•ʔっ <(Where would you like to go?) (type your X): "))
            break
        except ValueError:
            print("ʕ•ᴥ•ʔっ <(Oops! That was not a valid coord. Try again...)")
    while True:
        try:
            y = float(input("ʕ•ᴥ•ʔっ <(Where would you like to go?) (type your Y): "))
            break
        except ValueError:
            print("ʕ•ᴥ•ʔっ <(Oops! That was not a valid coord. Try again...)")
    while True:
        try:
            z = float(input("ʕ•ᴥ•ʔっ <(Where would you like to go?) (type your Z): "))
            break
        except ValueError:
            print("ʕ•ᴥ•ʔっ <(Oops! That was not a valid coord. Try again...)")     
    xyzf = round(x), round(y), round(z)
    print("""ʕ•ᴥ•ʔ <(Teleporting...)""")
    sleep(4)
    sp = mc.player.setPos(xyzf)
    pos = mc.player.getPos()
    xp = int(float(pos.x))
    yp = int(float(pos.y))
    zp = int(float(pos.z))
    playerpos = round(xp), round(yp), round(zp)
    if playerpos == xyzf:
        print("""ʕ•ᴥ•ʔ <(Teleport succesfull!)""")
    else:
        print("""ʕ•ᴥ•ʔ <(Teleport unccucesfull!)""")
    sleep(1)

# The finishing/continuing loopes
def MagicBearFcStart():
    while True:
        MagicBearFIP()
        o = input("""ʕ•ᴥ•ʔ <(Want to go somewhere else?) (y/n): """)
        if o == "n":
            print("""ʕ•ᴥ•ʔっ <(Goodbye)""")
            sleep(1)
            break
        if o == "y":
            print("""ʕ•ᴥ•ʔ" <(Going again...)
""")
            sleep(1)

 # The simplified starting point
MagicBearFcStart()