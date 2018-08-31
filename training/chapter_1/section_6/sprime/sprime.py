"""
ID: michael332
LANG: PYTHON3
TASK: sprime
"""

from math import sqrt
from time import time

start = time()

def check(n):
    if n == 1:
        return False
    for x in range(2, (int)(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def combinations(i, num, limit, list1, list2, fout):
    if i == limit:
        ifTrue = True
        dup = 0
        position = 0
        while position < limit:
            dup *= 10 
            dup += num[position]
            if check(dup) == False:
                ifTrue = False
                break
            else:
                position += 1
        if ifTrue == True:
            fout.write (str(dup) + '\n')
    else:
        if num == []:
            for j in list1:
                num.append(j)
                combinations(i+1, num, limit, list1, list2, fout)
                num.pop()
        else:
            for j in list2:
                num.append(j)
                combinations(i+1, num, limit, list1, list2, fout)
                num.pop()


fin = open("sprime.in", 'r')
fout = open("sprime.out", 'w')

num = int(fin.readline())

i = 0
number = []
first = [2, 3, 5, 7]
others = [1, 3, 7, 9]

combinations(i, number, num, first, others, fout)

fout.close()

print(time() - start)
