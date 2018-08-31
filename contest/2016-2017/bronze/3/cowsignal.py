fin = open ('cowsignal.in', 'r')
fout = open ('cowsignal.out', 'w')

rows, columns, multiply = fin.readline().strip().split()

rows = int(rows)
columns = int(columns)
multiply = int(multiply)
theLines = []

for i in range(rows):
    lines = fin.readline().strip()
    theLines.append(lines)

aString = '' 

for i in range(rows):
    for k in range(multiply):
        for j in range(columns):
            for l in range(multiply):
                if j == columns - 1:
                    if l == multiply - 1:
                        aString += theLines[i][j] + '\n'
                    else:
                        aString += theLines[i][j]
                else:
                    aString += theLines[i][j]

fout.write (str(aString))

fout.close
