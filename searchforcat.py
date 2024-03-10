import os
import time
import urllib.error
import googlesearch
os.system("title cat search")
website =input("what website do you want to search cats on (some websites might not work)\n")
cat = input("cats:\n")
f = open(website + " with cats.txt", "w")
f.write("if theres nothing in this file and you searched it means you hit a error\n")
numofresults =input("how many results do you want? \n")
input("press enter to start searching for cats\n")
import googlesearch
from googlesearch import search


def google_search(t):
    time.sleep(1)
    print("searching.. might take a while (because of error 429 :/)")
    print( "debug: "+ numofresults)
    print(int(numofresults))
    for results in search("cats" + cat + " site:" + website, tld="co.in", num=int(numofresults), stop=int(numofresults), pause=5):
        f.write("found results with " +cat +"\n")
        f.write(results + "\n")
        print("found: " + results + "\n")
time.sleep(1)

if int(numofresults) <= 100:

 google_search(t=0)

else:
 print("can not find results higher than 100")
time.sleep(1)
exit()