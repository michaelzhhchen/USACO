"""
ID: michael332
LANG: PYTHON3
TASK: transform
"""

fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')

Num = int(fin.readline())
def printArray(a):
    for e in a:
        print(e)

def rotate90Degrees(originalList):
    duplicateList = [[0] * Num for _ in range(Num)]
    for i in range(Num):
        for j in range(Num):
            duplicateList[j][Num-i-1] = originalList[i][j]
    return duplicateList

def mirror(originalList):
    duplicateList = [[0] * Num for _ in range(Num)]    
    for j in range(Num):
        for i in range(Num-1, -1, -1):
            duplicateList[j][Num-i-1] = originalList[j][i]        
    return duplicateList

original = []
transformed = []

for j in range(Num):
    line = fin.readline().strip()
    original.append(list(line))
for j in range(Num):
    line = fin.readline().strip()
    transformed.append(list(line))

mirrored = mirror(original)
D90 = rotate90Degrees(original)
D180 = rotate90Degrees(D90)
D270 = rotate90Degrees(D180)
MD90 = rotate90Degrees(mirrored)
MD180 = rotate90Degrees(MD90)
MD270 = rotate90Degrees(MD180)

x = 0

if D90 == transformed:
    x = 1
elif D180 == transformed:
    x = 2
elif D270 == transformed:
    x = 3
elif mirrored == transformed:
    x = 4
elif MD90 == transformed or MD180 == transformed or MD270 == transformed:
    x = 5
elif original == transformed:
    x = 6
else:
    x = 7

fout.write (str(x) + '\n')
fout.close
