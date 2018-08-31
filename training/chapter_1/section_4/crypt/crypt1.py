"""
ID: michael332
LANG: PYTHON3
TASK: crypt1 
"""

def keepAdding(numList, bigList, x):
    for i in range(len(bigList)):
        bigList[i].append(numList[i//x])
    return bigList

fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')

num = int(fin.readline().strip())
strs = fin.readline().strip().split()

ints = []
combinations = []

for i in range(len(strs)):
    ints.append(int(strs[i]))
    
for i in range(len(ints)):
    combinations.append([])

y = 1

for i in range(num):
    disposable = keepAdding(ints, combinations, y)
    combinations = disposable
    combinations *= num
    y *= num

valids = []

for i in range(len(combinations)):
    theIf = True
    x = []
    for j in range((len(combinations[i]) // 2) + len(combinations[i]) % 2):
        x.append(combinations[i][j])
    y = 0
    z = 0
    counter = 0
    for j in range(-1, len(x) - 1, -1):
        y += x[j] * 10^counter
        counter += 1
    counter = 0
    for j in range((len(combinations[i]) // 2) - 1 + len(combinations) % 2, len(combinations[i]) - 1, -1):
        z += combinations[j] * 10^counter
        counter += 1
    disposable = [int(d) for d in str(z)]
    for i in range(len(disposable)):
        if disposable[i] not in ints:
            theIf = False
    for j in range((len(combinations[i]) // 2) - 1 + len(combinations) % 2, len(combinations[i]) - 1, -1):
        variable = combinations[i][j] * y
        disposable = [int(d) for d in str(variable)]
        for i in range(len(disposable)):
            if disposable not in ints:
                theIf = False
                continue
    if theIf == True:
        valids.append(combinations[i])

print(valids)
print(combinations)
