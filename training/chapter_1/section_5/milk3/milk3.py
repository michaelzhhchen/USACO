"""
ID: michael332
LANG: PYTHON3
TASK: milk3
"""

def pour(oldList, newList, alreadyList):
    dup = [i for i in oldList]
    dupA = [i for i in alreadyList]
    for i in range(3):
        for j in range(3):
            oldList = [k for k in dup]
            alreadyList = [k for k in dupA]            
            if i != j:
                if oldList[j][0] - oldList[j][1] <= oldList[i][1]:
                    oldList[i][1] -= oldList[j][0] - oldList[j][1]
                    oldList[j][1] = oldList[j][0]
                else:
                    oldList[j][1] += oldList[i][1]
                    oldList[i][1] = 0
                if oldList[0][1] == 0:
                    if oldList[2][1] not in newList:
                        newList.append(oldList[2][1])
                if str(oldList) not in alreadyList:
                    alreadyList.append(str([k for k in oldList]))
                    pour(oldList, newList, alreadyList)

fin = open ("milk3.in", 'r')
fout = open ("milk3.out", 'w')

A, B, C = fin.readline().strip().split()

bigList = [[int(A), 0], [int(B), 0], [int(C), int(C)]]
dup = [i for i in bigList]
new = []
already = [str(dup)]

pour(dup, new, already)

print(new)

for i in range(len(new)):
    if i == len(new) - 1:
        fout.write (str(new[i]) + '\n')
    else:
        fout.write (str(new[i]) + ' ')

fout.close()
