"""
ID: michael332
LANG: PYTHON3
TASK: wormhole
"""

fin = open ("wormhole.in", 'r')
fout = open ("wormhole.out", 'w')

x = int(fin.readline())

List = []

for i in range(1, x+1):
    if x%i == 0 and i != 1 and i != x:
        List.append(i)

num = 1

for i in range(len(List)):
    num *= List[i]

fout.write(str(num) + '\n')

fout.close()
