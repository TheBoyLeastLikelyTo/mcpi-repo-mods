import mcpi.minecraft as minecraft
from time import sleep
from pynput import mouse
from pynput.mouse import Button, Controller
import pyautogui, pyperclip

mc = minecraft.Minecraft.create()
mouse = Controller()

def typeChar(message=pyperclip.paste(), form='chat'):
    if form == 'chat':
        mc.postToChat(message)
    if form == 'sign':
        mouse.press(Button.right)
        sleep(.1)
        mouse.release(Button.right)
        if message == '':
            message = pyperclip.paste()
        for i in range(0, int(len(message)/15)+1):
            if i == 0:
                pyautogui.write(message[(i*15):((i+1)*15)-1], interval=0.01)
            else:
                pyautogui.write(message[(i*15)-1:((i+1)*15)-1], interval=0.01)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')

def moveKey(keyPress, args=''):
    if args == '':
        pyautogui.keyDown(keyPress)
        sleep(.13)
        pyautogui.keyUp(keyPress)
    else:
        while not args:
            pyautogui.keyDown(keyPress)
        pyautogui.keyUp(keyPress)
    
sleep(2)
typeChar('hello this is a bot speaking', 'sign')
sleep(1)
moveKey('d')
typeChar('This bot can talk in two forms', 'sign')
moveKey('d')
sleep(1)
typeChar('With signs', 'sign')
sleep(2)
typeChar('and with chat', 'chat')
sleep(2)
typeChar('This bot can also move', 'chat')
moveKey('d')
sleep(1)
typeChar('soon the code will be on github', 'sign')
moveKey('d')
sleep(1)
typeChar('but first, it needs a name', 'sign')