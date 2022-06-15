import minecraft
import block
import time

x = raw_input("enter ip adress of your server ")

mc = minecraft.Minecraft.create(x, 4711)

print("this is an artificial chat program!")

print('to end your chat session say -end- to chat')

print("you have to say -end- two times in a row to confirm")

user = raw_input("enter your username --> ")

def get_text():
    text = raw_input("input text --> ")
    mc.postToChat(user + ": " + text)
    return text
    
while(True):
    get_text()
    if get_text() == "end":
        print("you have ended your chat session")
        mc.postToChat(user + " has ended his chat session")
        break
    
