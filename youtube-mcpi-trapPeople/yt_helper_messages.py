from mcpi.minecraft import Minecraft
from time import sleep
mc=Minecraft.create()


CHAT_MSGS = ['as you see,', 'this my world,', 'And my bro is going ',
             'To show up here soon', 'so in case they will break some',
             'of my stuff, I can trap them in my prison',
             'and make the world immutable', 'the code is as always found on',
             'github, link in description.',
             'this is also written by a program. same repository',
             'so lets stop talking and run the program,',
             'i am using multiple minecraft pi windows,',
             'so i have another person in my world.',
             'running the code']

for msg in CHAT_MSGS:
    mc.postToChat('<LEHAtupointow>: ' + msg)
    sleep(1)

sleep(6)
print('done')
