"""
ID: michael332
LANG: PYTHON3
TASK: palsquare
"""

def base(numbers, squares, convo):
    x = True
    count = 0
    number = []
    while x != False:
        print(squares, numbers)
        number.append(convo[squares % numbers]) 
        squares -= squares % numbers
        squares = squares//numbers
        print(number)
        if squares == 0:
            x = False
        else: 
            count += 1
    return number[::-1]

fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')

conversionDict = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G", 17:"H", 18:"I", 19:"J"}

num = int(fin.readline())
pals = []

for i in range(1, 301):
    digits = []
    square = i*i
    x = base(num, square, conversionDict)
    y = base(num, i, conversionDict)
    if x == x[::-1]:
        x2 = "".join(x)
        y2 = "".join(y)
        pals.append([y2, x2])
    

for i in range(len(pals)):
    fout.write (str(pals[i][0]) + " " + str(pals[i][1]) + '\n')

fout.close()
