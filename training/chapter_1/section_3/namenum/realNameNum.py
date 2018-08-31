"""
ID: michael332
LANG: PYTHON3
TASK: namenum
"""
def conversionChart(variable):
    if variable == "2": 
        return ['A', 'B', 'C']
    if variable == "3":
        return ["D", "E", "F"]
    if variable == "4":
        return ["G", "H", "I"]
    if variable == "5":
        return ["J", "K", "L"]
    if variable == "6":
        return ["M", "N", "O"]
    if variable == "7":
        return ["P", "R", "S"]
    if variable == "8":
        return ["T", "U", "V"]
    if variable == "9":
        return ["W", "X", "Y"]

def threeTimesList(aList):
    aList *= 3
    return aList

def keepAdding(number, bigList, x):
    for i in range(len(bigList)):
        bigList[i] += (conversionChart(number))[i//x]
    return bigList

fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')

num = str(fin.readline().strip())
theList = list(num)
hugeList = ["", "", ""]

print(theList)
y = 1

for x in range(len(num)):
    hugeList = keepAdding(theList[x], hugeList, y)
    hugeList = threeTimesList(hugeList)
    y *= 3


with open('dict.txt', 'r') as fin1:
    cowNames = {i.rstrip() for i in fin1}

namesList = []

for i in range(len(hugeList)):
    if hugeList[i] in cowNames:
        print(hugeList[i])
        if hugeList[i] not in namesList:
            namesList.append(hugeList[i])
        else:
            continue
    else:
        continue

if len(namesList) == 0:
    fout.write('NONE' + '\n')
else:
    namesList.sort()
    for i in range(len(namesList)):
        fout.write(str(namesList[i]) + '\n')

fout.close()
