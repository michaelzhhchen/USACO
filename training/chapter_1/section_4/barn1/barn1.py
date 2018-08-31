"""
ID: michael332
LANG: PYTHON3
TASK: barn1
"""

fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')

boards, stalls, cows = fin.readline().strip().split()

boards = int(boards)
stalls = int(stalls)
cows = int(cows)

cowList = []

if boards > cows:
    boards = cows

for i in range(cows):
    cow = int(fin.readline())
    cowList.append(cow)

cowList.sort()

differenceList = []

for i in range(1, cows):
    differenceList.append(cowList[i] - cowList[i-1])
print(differenceList)
differenceList.sort()
print(differenceList)
biggestOnes = []

print(len(differenceList) - boards - 1)


for i in range(boards-1):
    x = len(differenceList) - i - 1
    biggestOnes.append(differenceList[x])

print(biggestOnes)

stalls -= stalls - cowList[cows - 1]
stalls -= cowList[0] - 1 

for i in range(len(biggestOnes)):
    stalls -= biggestOnes[i] - 1

print(stalls)

fout.write (str(stalls) + '\n')
fout.close()
