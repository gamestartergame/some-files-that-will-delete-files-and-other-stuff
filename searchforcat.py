import os
import time
import urllib.error
import googlesearch
cat =input("what cat related thing you want to search?(dont include cats)\n")
os.system("title cat search")
f =open("youtube with cats.txt" , "w")
input("press enter to start searching for cats\n")
print("searching.. might take a while (because of error 429 :/)")
from googlesearch import search
for results in search("cats" + cat +"site:youtube.com" , tld="co.in" , num=50, stop=50 , pause=20):


 f.write(results + "\n")
 print("cat search done")
 y_n =input("do you want to open one? y or n\n")
 if y_n == "y":
  print("opening")
 os.system("start " + results + "\n")

