from mcpi.minecraft import Minecraft
import tkinter as tk

'#Creator Red-exe-Engineer/Wallee'

mc = Minecraft.create()
x, y, z = mc.player.getPos()
easyBreak = 0

root = tk.Tk()

def Btn1Pressed():
    print(1)
    mc.player.setPos(-97, 1, 98.5)


def Btn2Pressed():
    print(2)
    global easyBreak
    if easyBreak == 1:
        easyBreak = 0
    else:
        easyBreak = 1
    print(easyBreak)

    x, y, z = mc.player.getPos()
    mc.setBlock(x, y-1, z, 20)


def Btn3Pressed():
    mc.player.setPos(-13.5, -62, -38.5)


def Btn4Pressed():
    print(4)
    mc.player.setPos(0.5, 1+mc.getHeight(0, 0), 0.5)


canvas = tk.Canvas(root, width=500, height=25)
canvas.grid(columnspan=4)


instructions = tk.Label(root, text="                                Server Hacks")
'#It works, ok...'
instructions.grid(columnspan=3, column=0, row=1)

#instructions = tk.Label(root, text="Creative Hacks")
#instructions.grid(columnspan=3, column=0, row=1)

button = tk.StringVar()
btn = tk.Button(root, textvariable=button, command=lambda:Btn2Pressed(), height=2, width=10)
button.set("Easy Break")
btn.grid(column=1, row=2)


instructions.grid(columnspan=3, column=0, row=1)

button = tk.StringVar()
btn = tk.Button(root, textvariable=button, command=lambda:Btn3Pressed(), height=2, width=10)
button.set("Stash")
btn.grid(column=2, row=2)


instructions.grid(columnspan=3, column=0, row=1)

button = tk.StringVar()
btn = tk.Button(root, textvariable=button, command=lambda:Btn1Pressed(), height=2, width=10)
button.set("TP to Base")
btn.grid(column=0, row=2)


instructions.grid(columnspan=3, column=0, row=1)

button = tk.StringVar()
btn = tk.Button(root, textvariable=button, command=lambda:Btn4Pressed(), height=2, width=10)
button.set("TP to Mid")
btn.grid(column=3, row=2)


if easyBreak == 1:
    print("True")

root.mainloop()