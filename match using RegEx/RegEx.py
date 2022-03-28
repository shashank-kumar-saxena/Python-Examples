import re
hand=open("D:\Python Examples\match using RegEx\Document.txt")
numlist=list()
for line in hand:
    stuff=re.findall("([0-9.]+)", line)
    if len(stuff)!=1:
        continue
    num=float(stuff[0])
    numlist.append(num)
print(max(numlist))