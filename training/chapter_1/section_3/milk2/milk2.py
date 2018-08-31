"""
ID: michael332
LANG: PYTHON3
TASK: milk2
"""
fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
firsts = []
lasts = []
Num = int(fin.readline())
for x in range(Num):
    first,last = list(map(int, fin.readline().split()))
    firsts.append(first)
    lasts.append(last)

theLongOne = []

for i in range(Num):
    for j in range(lasts[i] - firsts[i]):
        theLongOne.append(j + firsts[i])

maxnumber = 0

for i in range(len(theLongOne)):
    if i == 0:
        continue
    else:
        if maxnumber < theLongOne[i] - theLongOne[i-1]:
            maxnumber = theLongOne[i] - theLongOne[i-1]

count = 0
counts = []

for i in range(len(theLongOne)):
    if i == 0:
        continue
    else:
        if theLongOne[i] == theLongOne[i-1] + 1:
            count += 1
        elif theLongOne[i] == theLongOne[i-1]:
            continue
        else:
            counts.append(count)
            count = 0

if len(counts) == 0:
    finalCount = theLongOne[len(theLongOne) - 1] - theLongOne[0]
else:
    finalCount = max(counts)

fout.write (str(finalCount + 201) + ' ' + str(maxnumber - 1))
fout.close()

