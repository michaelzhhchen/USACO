"""
ID: michael332
LANG: PYTHON3
TASK: beads
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')

def optimization(looping_amount, original_string, num_list, color_list):
    for i in range(looping_amount):
        if i == 0:
            x = original_string[i]
            y = 1
        else:
            if original_string[i] == x[0]:
                y += 1
            else:
                color_list.append(x)
                num_list.append(y)
                x = original_string[i]
                y = 1

N = int(fin.readline())
Color = fin.readline().strip()
Colors = Color * 2
combinedColors = []
combinedNums = []

optimization(N*2, Colors, combinedNums, combinedColors)

aNewColorList = []
aNewNumList = []

for i in range(len(combinedColors)):
    if i != 0 and i != len(combinedColors) - 1 and combinedColors[i] == 'w' \
    and combinedColors[i+1] == combinedColors[i-1]:
            aNewColorList.append(combinedColors[i-1])
            aNewNumList.append(combinedNums[i])
    else:
            aNewColorList.append(combinedColors[i])
            aNewNumList.append(combinedNums[i])


newColors = ""

for x in range(len(aNewColorList)):
    for i in range(aNewNumList[x]):
        newColors += aNewColorList[x]


finalOptimizationColors = []
finalOptimizationNums = []

optimization(len(newColors), newColors, finalOptimizationNums, finalOptimizationColors)


max_value = 0

current_value = 0

print("Nums: ", finalOptimizationNums)
print("Colors: ", finalOptimizationColors)

for i in range(len(finalOptimizationNums)):
    if i == 0 or i == len(finalOptimizationNums) - 1:
        continue
    elif finalOptimizationColors[i] == 'w':
        backwardsValue = finalOptimizationNums[i-1]
        forwardsValue = finalOptimizationNums[i+1]
        print("i=", i, " backwardsValue=", backwardsValue)
        notSame = True
        x = 0
        while notSame == True:
            if i-x-2 < 0:
                notSame = False
                print("log1")
            elif finalOptimizationColors[i-x-2] == finalOptimizationColors[i-1]:
                notSame = False
                print("log2")
            else:
                backwardsValue += finalOptimizationNums[i-x-2]
                print("log3")
            x += 1

        print("i=", i, " backwardsValue=", backwardsValue)
        notSame = True
        x = 0
        while notSame == True:
            if i+x+2 > len(finalOptimizationNums) - 1:
                notSame = False
            elif finalOptimizationColors[i+x+2] == finalOptimizationColors[i+1]:
                notSame = False
            else:
                forwardsValue += finalOptimizationNums[i+x+2]
            x += 1
        print("i=", i, " forwardsValue=", forwardsValue)
        if backwardsValue >= forwardsValue:
            current_value = backwardsValue
        else:
            current_value = forwardsValue
        current_value += finalOptimizationNums[i]
    else:
        current_value = finalOptimizationNums[i] + finalOptimizationNums[i-1]
        print("i=", i, " current_value=", current_value)
    print("comparing current_value=", current_value, " max_value=", max_value)
    if current_value > max_value:
        max_value = current_value
        print("new max_value=", max_value)

if max_value == 0:
    max_value = len(Color)
else:
    max_value = max_value    

fout.write (str(max_value) + '\n')
fout.close()

