"""
ID: michael332
LANG: PYTHON3
TASK: namenum
"""

from itertools import product

fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')

with open('dict.txt', 'r') as fin1:
    cowNames = {i.rstrip() for i in fin1}

def chooser(theList, listIndex):
    list2 = ['A', 'B', 'C']
    list3 = ['D', 'E', 'F']
    list4 = ['G', 'H', 'I']
    list5 = ['J', 'K', 'L']
    list6 = ['M', 'N', 'O']
    list7 = ['P', 'R', 'S']
    list8 = ['T', 'U', 'V']
    list9 = ['W', 'X', 'Y']
    if theList[listIndex] == 2:
        return list2
    elif theList[listIndex] == 3:
        return list3
    elif theList[listIndex] == 4:
        return list4
    elif theList[listIndex] == 5:
        return list5
    elif theList[listIndex] == 6:
        return list6
    elif theList[listIndex] == 7:
        return list7
    elif theList[listIndex] == 8:
        return list8
    elif theList[listIndex] == 9:
        return list9


x = fin.readline().strip()
x = str(x)
digitList = []

for i in range(len(x)):
   digitList.append(int(x[i]))

listList = []

for i in range(len(digitList)):
    listList.append(chooser(digitList, i))

names = set(''.join(i) for i in (product(*listList)))

goodNames = sorted(list(names&cowNames))

if goodNames == []:
    fout.write('NONE' + '\n')
else:
    for i in range(len(goodNames)):
        fout.write(str(goodNames[i]) + '\n')

fout.close
