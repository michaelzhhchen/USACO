"""
ID: michael332
LANG: PYTHON3
TASK: friday
"""

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

num = int(fin.readline())
week_days = [0, 0, 0, 0, 0, 0, 0]
year = 1900

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x = 0

for j in range(num):
    if (year + j) % 100 == 0:
        if (year + j) % 400 == 0:
            daysInMonth[1] = 29
        else:
            daysInMonth[1] = 28
    else:
        if (year + j) % 4 == 0:
            daysInMonth[1] = 29
        else:
            daysInMonth[1] = 28
    for i in range(12):
        week_days[x] += 1 
        x += daysInMonth[i]
        x %= 7
        print("i = ", i, " x = ", x)

for i in range(6):
    fout.write (str(week_days[i]) + " ")

fout.write (str(week_days[6]) + "\n")

fout.close()
