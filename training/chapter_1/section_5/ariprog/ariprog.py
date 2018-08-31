"""
ID: michael332
LANG: PYTHON3
TASK: ariprog
"""

import time

start = time.time()

fin = open("ariprog.in", 'r')
fout = open("ariprog.out", 'w')

length = int(fin.readline())
limit = int(fin.readline())

squares = []

for i in range(limit + 1):
    squares.append(i**2)

bisquares = []

for i in range(limit + 1):
    for j in range(limit + 1):
        if squares[i] + squares[j] not in bisquares:
            bisquares.append(squares[i] + squares[j])

bisquares.sort()

differences = []

for i in range(1, (squares[-1] + squares[-1])//(length-2)):
    for j in range(len(bisquares)):
        localList = []
        count = 0
        for k in range(length):
            var = bisquares[j] + (k * i)
            if var in bisquares:
                localList.append(var)
                count += 1
            else:
                break
        if count == length:
            differences.append([i, bisquares[j]])

differences.sort()

if differences == []:
    fout.write ("NONE" + '\n')
else:
    for i in range(len(differences)):
        fout.write (str(differences[i][1]) + " " + str(differences[i][0]) + '\n')

fout.close()

print(time.time() - start)
