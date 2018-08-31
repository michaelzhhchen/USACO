"""
ID: michael332
LANG: PYTHON3
TASK: gift1
"""
people = {}
with open("gift1.in") as fin:
    lines = fin.readlines()
population = (int(c) for c in lines[0].split())
for i in range(population):
    x = (int(x) for x in lines[i+1].split())
    people[x] = 1
listcounter= population + 1
for j in range(len(people)):
    listcounter += 1
    x = (int(x) for x in lines[listcounter])
    listcounter += 1
    y = (int(x) for x in lines[listcounter])
    y[0] = y[0] - (y[0] % y[1])
    people[x] -= y
    for i in range(y[1]):
        listcounter += 1
        x = (int(x) for x in lines[listcounter])
        people[x] = y[0]+y[1]


fout = open ('gift1.out', 'w')

fout.write (str(people) + '\n')

fout.close