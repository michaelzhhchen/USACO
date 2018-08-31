"""
ID: michael332
LANG: PYTHON3
TASK: milk3
"""

def pour(already, capacity, load, new):
    already.append([k for k in load])
    dupLoad = [i for i in load]
    dupAlready = [i for i in already]
    for i in range(3):
        for j in range(3):
            load = [k for k in dupLoad]
            already = [k for k in dupAlready]
            if i != j:
                if capacity[j] - load[j] <= load[i]:
                    load[i] -= capacity[j] - load[j]
                    load[j] = capacity[j]
                else:
                    load[j] += load[i]
                    load[i] = 0
            if load[0] == 0:
                if load[2] not in new:
                    new.append(load[2])
            if load not in already:
                pour(already, capacity, load, new)

fin = open ("milk3.in", 'r')
fout = open ("milk3.out", 'w')

A, B, C = fin.readline().strip().split()

capacity = [int(A), int(B), int(C)]
load = [0, 0, int(C)]

alreadyList = []
Cs = []

pour(alreadyList, capacity, load, Cs)

Cs.sort()

for i in range(len(Cs)):
    if i == len(Cs) - 1:
        fout.write (str(Cs[i]) + '\n')
    else:
        fout.write (str(Cs[i]) + ' ')

fout.close()
