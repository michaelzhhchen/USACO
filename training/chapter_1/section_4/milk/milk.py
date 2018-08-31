"""
ID: michael332
LANG: PYTHON3
TASK: milk
"""

fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')

amount, num = fin.readline().strip().split()

amount = int(amount)
num = int(num)

farmers = []

for i in range(num):
    cost, units = fin.readline().strip().split()
    farmers.append([int(cost), int(units)])

farmers.sort()

price = 0
stock = 0

while stock < amount:
    if stock + farmers[0][1] <= amount:
        price += farmers[0][0] * farmers[0][1]
        stock += farmers[0][1]
        del farmers[0]
    else:
        price += farmers[0][0] * (amount - stock)
        stock = amount

fout.write (str(price) + '\n')
fout.close
