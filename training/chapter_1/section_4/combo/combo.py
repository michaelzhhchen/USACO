"""
ID: michael332
LANG: PYTHON3
TASK: combo
"""

def combinations(bigSet, list1, localString, i):
    if i == 3:
        localString.strip()
        bigSet.add(localString)
    else:
        localVariable = localString
        for number in list1[i]:
            localString = localVariable
            localString += str(number) + " "
            combinations(bigSet, list1, localString, i+1)

fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')

num = int(fin.readline())
john1, john2, john3 = fin.readline().strip().split()
master1, master2, master3 = fin.readline().strip().split()

johns = [john1, john2, john3]
masters = [master1, master2, master3]

johnList = [[], [], []]
masterList = [[], [], []]



for i in range(3):
    for j in range(-2, 3):
        ifTrue = False
        variable = int(johns[i])
        while ifTrue == False:
            if variable + j < 1:
                variable += num
            elif variable + j > num:
                variable -= num
            else:
                johnList[i].append(variable + j)
                ifTrue = True
            print(variable)

for i in range(3):
    for j in range(-2, 3):
        ifTrue = False
        variable = int(masters[i])
        while ifTrue == False:
            if variable + j < 1:
                variable += num
            elif variable + j > num:
                variable -= num
            else:
                masterList[i].append(variable + j)
                ifTrue = True
            print(variable)

print(johnList)
print(masterList)

i = 0
sets = set()
localString = ""

combinations(sets, johnList, localString, i)
combinations(sets, masterList, localString, i)


fout.write (str(len(sets)) + '\n')

fout.close()
