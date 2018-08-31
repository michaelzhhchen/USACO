"""
ID: michael332
LANG: PYTHON3
TASK: skidesign
"""

fin = open ("skidesign.in", 'r')
fout = open ("skidesign.out", 'w')

num = int(fin.readline())

hillHeights = []

for i in range(num):
    hillHeights.append(int(fin.readline()))

hillHeights.sort()

aRange = hillHeights[-1] - hillHeights[0]

cost = -1

for i in range(aRange - 17):
    localCost = 0
    mini = i + hillHeights[0]
    maxi = mini + 17
    for j in range(num):
        if mini <= hillHeights[j] <= maxi:
            continue
        else:
            if hillHeights[j] < mini:
                localCost += (mini-hillHeights[j]) ** 2
            else:
                localCost += (hillHeights[j] - maxi) ** 2
    if localCost < cost:
        cost = localCost
    elif cost == -1:
        cost = localCost

if cost == -1:
    cost = 0

fout.write(str(cost) + '\n')

fout.close()
