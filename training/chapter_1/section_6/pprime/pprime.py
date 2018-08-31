"""
ID: michael332
LANG: PYTHON3
TASK: pprime
"""

import time

from math import sqrt

start = time.time()


def nums(j, num, i, limit, bigList, low, high, firstTerm, localTerm, localNum):
    num = localNum
    firstTerm = localTerm
    num += str(j)
    firstTerm = False
    palindromes(num, i+1, limit, bigList, low, high, firstTerm)

def palindromes(num, i, limit, bigList, low, high, firstTerm):
    if i == limit // 2 and limit % 2 == 0:
        num += num[::-1]
        if low <= int(num) <= high:
            bigList.append(int(num))
    elif i == limit//2 + limit % 2:
        back = num[::-1]
        for j in range(1, len(back)):
            num += back[j]
        if low <= int(num) <= high:
            bigList.append(int(num))
    else:
        localNum = num
        localTerm = firstTerm
        if firstTerm == True:
            if limit == len(str(low)):
                for j in range(int(str(low)[0]), 10):
                    if j % 2 == 1:
                        nums(j, num, i, limit, bigList, low, high, firstTerm, localTerm, localNum)
            elif limit == len(str(high)):
                for j in range(0, int(str(high)[0]) + 1):
                    if j % 2 == 1:
                        nums(j, num, i, limit, bigList, low, high, firstTerm, localTerm, localNum)
            else:
                for j in range(0, 10):
                    if j % 2 == 1:
                        nums(j, num, i, limit, bigList, low, high, firstTerm, localTerm, localNum)
        else:
            for j in range(0, 10):
                nums(j, num, i, limit, bigList, low, high, firstTerm, localTerm, localNum)

def check(n):
    if n == 1:
        return False
    for x in range(2, (int)(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

fin = open("pprime.in", 'r')
fout = open("pprime.out", 'w')

low, high = fin.readline().strip().split()

low = int(low)
high = int(high)

pals = []

minLength = len(str(low))
maxLength = len(str(high)) 

for j in range(minLength, maxLength + 1):
    num = ""
    i = 0
    firstTerm = True
    palindromes(num, i, j, pals, low, high, firstTerm)

print("Combinations: ", time.time() - start)

start = time.time()

for i in range(len(pals)):
    if check(pals[i]) == True:
        fout.write (str(pals[i]) + '\n')
    
print("Prime: ", time.time() - start)

fout.close()

print(time.time() - start)
