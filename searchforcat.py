import os
import time
import urllib.error
import googlesearch
os.system("title cat search")
cat =input("what cat related thing you want to search?(dont include cats)\n")
f =open("youtube with cats.txt" , "w")
input("press enter to start searching for cats\n")
print("searching.. might take a while (because of error 429 :/)")
import googlesearch
from googlesearch import search
def google_search(t):
 time.sleep(1)
 for results in search("cats" + cat +" site:youtube.com" , tld="co.in" , num=10  ,stop=10 , pause=5):
  f.write(results + "\n")
  print("found: " + results + "\n")
time.sleep(1)
exit()



google_search(t=0)