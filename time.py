from gtts import gTTS
import time
import os
print ("--------------------------------")
print ("|=======+ Sleep WATCH +========|")
print ("--------------------------------")
l = int(input('Enter time`~`: '))
for i in range(l,0,-1):
     print (i)
     time.sleep(1.0)
Text = 'time up boss time up boss time up boss'
language ='en'
output = gTTS(text = Text,lang=language)
output.save("time.mp3")
os.system('mpv /data/data/com.termux/files/home/project/time.mp3')
from time import sleep as sp
def timeup():
  for h in f"\n\n\t\t\t\t":
    print(h, end="", flush=True)
    sp(.1)
  story = f"""

  Made by Ro706
  PLEASE GIVE ME A ⭐ FOR MY MOTIVATION
  Thank u

  """.title()
  for i in list(story):
    print(i, end="", flush=True)
    sp(.1)

timeup()


