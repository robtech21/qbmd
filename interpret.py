import sys,os

os.system("cls")

with open("mdcode") as f:
    lines = f.readlines()
    f.close()
f = open("outcode",'a')
for p in lines:
    print("Original: "+str(p))
    p = p.replace("PNT","print").replace("PFL","printflush").replace("RD","read").replace("WR","write")
    print("New: "+str(p))
    f.write(p)
f.close()

