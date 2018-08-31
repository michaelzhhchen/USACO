"""
ID: michael332
LANG: PYTHON3
TASK: numtri
"""

fin = open("numtri.in", 'r')
fout = open("numtri.out", 'w')

num = int(fin.readline())

rows = []

for i in range(num):
    variable = fin.readline().strip().split()
    rows.append(variable)
    for j in range(len(variable)):
        rows[i][j] = [int(rows[i][j]), 0]

rows[0][0][1] = rows[0][0][0]

for i in range(1, num):
    for j in range(len(rows[i])):
        if j == 0:
            rows[i][j][1] = rows[i][j][0] + rows[i-1][j][1]
        elif j == len(rows[i]) - 1:
            rows[i][j][1] = rows[i-1][j-1][1] + rows[i][j][0]
        else:
            if rows[i-1][j][1] >= rows[i-1][j-1][1]:
                rows[i][j][1] = rows[i-1][j][1] + rows[i][j][0]
                
            else:
                rows[i][j][1] = rows[i-1][j-1][1] + rows[i][j][0]

maxNumber = 0

for i in range(len(rows[-1])):
    if rows[-1][i][1] > maxNumber:
        maxNumber = rows[-1][i][1]

fout.write (str(maxNumber) + '\n')

fout.close
