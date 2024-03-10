import os

import googlesearch
os.system("title cat search")
f =open("youtube with cats.txt" , "w")
input("press enter to start searching for cats\n")
print("searching.. might take a while (if crashes ever is a error or too many requests)")
from googlesearch import search
for results in search("cats site:youtube.com" , tld="co.in" , num=500, stop=500 , pause=5):
 f.write(results + "\n")
 print("cat search done")
 y_n =input("do you want to open one? y or n\n")
 if y_n == "y":
  print("opening")
 os.system("start " + results + "\n")