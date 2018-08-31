fin = open ('square.in', 'r')
fout = open ('square.out', 'w')

vertical = []
horizontal = []
for x in range(2):
    x1, y1, x2, y2 = fin.readline().strip().split()
    vertical.append(int(y2))
    vertical.append(int(y1))
    horizontal.append(int(x2))
    horizontal.append(int(x1))

x = max(vertical) - min(vertical)
y = max(horizontal) - min(horizontal)

maximum = 0

if x > y:
    maximum = x * x
else:
    maximum = y * y

fout.write (str(maximum) + '\n')
