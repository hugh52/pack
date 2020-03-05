#!/home/william/anaconda3/bin/python


import re


pth = "/home/william/Desktop/"

with open(pth + "packsone.txt", "r+") as f:
    pn = f.readlines()

la = []

for i in range(len(pn)):
    pat = re.compile(r"\w+")
    maob = pat.search(str(pn[i]))
    la.append(maob.group())
    i += 1

with open(pth + "packsnew.txt", "w+") as fil:
    for item in la:
        fil.write(str(item).replace("'", "") + "\n")
