"""
ID: michael332
LANG: PYTHON3
TASK: dualpal
"""

def base(numbers, integers):
    x = True
    count = 0
    number = []
    while x != False:
        number.append([integers % numbers]) 
        integers -= integers % numbers
        integers = integers//numbers
        if integers == 0:
            x = False
        else: 
            count += 1
    if number == number[::-1]:
        return number[::-1]
        print(number)
    else:
        return None

fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')

amount, starting = fin.readline().split()

amount = int(amount)
starting = int(starting)

count = 1
loop_out = False
num_list = []

while loop_out == False:
    counter = []
    for i in range(2, 11):
        if base(i, starting+count) != None:
            counter.append(base(i, starting+count))
        if len(counter) == 2:
            num_list.append(starting + count)
            print(num_list.append) 
            break
    if len(num_list) == amount:
        loop_out = True
    count += 1

for i in range(amount):
    fout.write (str(num_list[i]) + '\n')

fout.close
