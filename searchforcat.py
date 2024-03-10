import os
import time
import urllib.error
import googlesearch
os.system("title cat search")
website =input("what website do you want to search cats on\n")
cat = input("cats:\n")
f = open("youtube with cats.txt", "w")
f.write("if theres nothing in this file and you searched it means you hit a error")
input("press enter to start searching for cats\n")
print("searching.. might take a while (because of error 429 :/)")
import googlesearch
from googlesearch import search


def google_search(t):
    time.sleep(1)
    for results in search("cats" + cat + " site:" + website, tld="co.in", num=10, stop=10, pause=5):
        f.write(results + "\n")
        print("found: " + results + "\n")
time.sleep(1)



google_search(t=0)
