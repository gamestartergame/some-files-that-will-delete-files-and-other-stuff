import os
import time
import urllib.error
import googlesearch
import subprocess
os.system("title cat search (made by gamestartergame)")
print("github: https://github.com/gamestartergame")
print("youtube: https://www.youtube.com/channel/UCk7nqcjq4od5hbf039Vn2QQ")
website =input("what website do you want to search cats on (some websites might not work)\n")
cat = input("cats:\n")
f = open(website + " with cats.txt", "w")
f.write("if theres nothing in this file and you searched it means you hit a error\n")
numofresults =input("how many results do you want? \n")
input("press enter to start searching for cats\n")
print("opening console for debug")
cmd = subprocess.Popen("cmd.exe /K cd c:/")
import googlesearch
from googlesearch import search


def google_search(count):

 time.sleep(1)
 print("searching.. might take a while (because of error 429 :/)")
 print( "debug: "+ numofresults)
 print(int(numofresults))
 for res in search("cats" + cat + " site:" + website, tld="co.in", num=int(numofresults), stop=int(numofresults), pause=5):
  count = count + 1
  f.write("found results with "+ cat +" result number: "+ str(count) +"\n")
  f.write(res + "\n")
  print("found: " + res +" "+ str(count) +"\n")
 cmd.terminate()
 time.sleep(1)




if int(numofresults) <= 200:

 google_search(count=0)

else:
 print("can not find results higher than 200")
time.sleep(1)