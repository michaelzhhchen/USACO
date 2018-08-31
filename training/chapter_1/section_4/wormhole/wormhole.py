"""
ID: michael332
LANG: PYTHON3
TASK: wormhole
"""
import time

start = time.time()
result = 0
count = 0

def checkDifferentLines(combList, dictionary, list2, x):
    for j in range(x):
        position = combList[j]
        original = combList[j]
        localTrue = False
        ifTrue = False
        while localTrue == False:
            position = list2[dictionary.index(position)]
            if position == None:
                localTrue = True
            else:
                pos = combList.index(position)
                if pos % 2 == 1:
                    position = combList[pos - 1]
                else:
                    position = combList[pos + 1]
                if position == original:
                    global result
                    result += 1
                    localTrue = True
                    ifTrue = True
        if ifTrue == True:
            break

def adding(localList, x, j, combinations, i, dictionary, list2, p1, p2):
    p2 = p1
    p1 = j
    localList.append(j)
    combinations(x, localList, i+1, dictionary, list2, p1, p2)
    localList.pop()

def combinations(x, localList, i, dictionary, list2, p1, p2):
    if i == x:
        checkDifferentLines(localList, dictionary, list2, x)
    else:
        for j in range(x):
            if j not in localList:
                if i % 2 == 1:
                    if j > p1:
                        adding(localList, x, j, combinations, i, dictionary, list2, p1, p2)
                else:
                    if i == 0:
                        adding(localList, x, j, combinations, i, dictionary, list2, p1, p2)
                    elif j > p2:
                        adding(localList, x, j, combinations, i, dictionary, list2, p1, p2)
                        
fin = open ("wormhole.in", 'r')
fout = open ("wormhole.out", 'w')

num = int(fin.readline())
coordinates = []

for i in range(num):
    x, y = fin.readline().strip().split()
    coordinates.append([int(x), int(y)])

list2 = []
validWormholes = []

for i in range(num):
    listIndex = None 
    for j in range(num):
        if coordinates[j][1] == coordinates[i][1]:            
            if listIndex == None:
                if coordinates[j][0] - coordinates[i][0] > 0:
                    listIndex = j
            elif coordinates[listIndex][0] - coordinates[i][0] > coordinates[j][0] - coordinates[i][0] > 0: 
                listIndex = j
    validWormholes.append(i)
    list2.append(listIndex)

i = 0
localList = []
x = num
p1 = 0
p2 = 0

combinations(x, localList, i, validWormholes, list2, p1, p2)


fout.write (str(result) + '\n')

fout.close()

print(time.time() - start)
