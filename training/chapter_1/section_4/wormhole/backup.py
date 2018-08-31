"""
ID: michael332
LANG: PYTHON3
TASK: wormhole
"""

import time

def checkDifferentLines(combList, loopList, dictionary):
    for j in range(len(combList)):
        localList = []
        position = combList[j]
        localTrue = False
        while localTrue == False:
            position = dictionary[str(position)]
            if position == None:
                localTrue = True
                continue
            else:
                if combList.index(position) % 2 == 1:
                    position = combList[combList.index(position) - 1]
                else:
                    position = combList[combList.index(position) + 1]
            if position not in localList:
                if position != None:
                    localList.append(position)
            else:
                if combList not in loopList:
                    loopList.append([i for i in combList])
                localTrue = True

def adding(localList, list1, j, combinations, i, num, bigList, dictionary):
        localList.append(list1[j])
        combinations(bigList, list1, localList, i+1, num, dictionary)
        localList.pop()

def combinations(bigList, list1, localList, i, num, dictionary):
    if i == num:
        checkDifferentLines(localList, bigList, dictionary)
    else:
        for j in range(len(list1)):
            if list1[j] not in localList:
                if len(localList) % 2 == 1:
                    if list1[j] > localList[-1]:
                        adding(localList, list1, j, combinations, i, num, bigList, dictionary)
                else:
                    if len(localList) == 0:
                        adding(localList, list1, j, combinations, i, num, bigList, dictionary)
                    elif list1[j] > localList[-2]:
                        adding(localList, list1, j, combinations, i, num, bigList, dictionary)
                        
fin = open ("wormhole.in", 'r')
fout = open ("wormhole.out", 'w')

num = int(fin.readline())
coordinates = []
intCoordinates = []

for i in range(num):
    x, y = fin.readline().strip().split()
    coordinates.append([int(x), int(y)])

validWormholes = {}

for i in range(num):
    listIndex = -1
    for j in range(num):
        if coordinates[i] == coordinates[j]:
            continue
        else:
            if coordinates[j][1] == coordinates[i][1]:            
                if coordinates[listIndex][0] - coordinates[i][0] > coordinates[j][0] - coordinates[i][0] and coordinates[j][0] - coordinates[i][0] > 0: 
                    listIndex = j
                elif listIndex == -1 and coordinates[j][0] - coordinates[i][0] > 0:
                    listIndex = j
                else:
                    continue
            else:
                continue
    if listIndex == -1:
        listIndex = None
    else:
        listIndex = coordinates[listIndex]
    validWormholes[str(coordinates[i])] = listIndex


start = time.time()

i = 0
localList = []
combinationList1 = []

combinations(combinationList1, coordinates, localList, i, num, validWormholes)

print(time.time() - start)

fout.write (str(len(combinationList1)) + '\n')

fout.close()




