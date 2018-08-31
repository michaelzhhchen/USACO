"""
ID: michael332
LANG: PYTHON3
TASK: crypt1 
"""

fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')

def findNums(i, result, numList, substr1, substr2):
  if i == 5:
    result.append([substr1, substr2])
  else:
    local1 = substr1
    local2 = substr2
    for digit in numList:
      substr1 = local1
      substr2 = local2
      if i <= 5//2:
        substr1 += digit
      else:
        substr2 += digit
      findNums(i+1, result, numList, substr1, substr2)

num = int(fin.readline().strip())
digits = fin.readline().strip().split()

substr1 = ""
substr2 = ""
numbers = []
findNums(0, numbers, digits, substr1, substr2)

print(len(numbers))

for i in range(len(numbers)):
  numbers[i][0] = int(numbers[i][0])
  numbers[i][1] = [int(d) for d in str(numbers[i][1])]

valids = []


print(digits)
for i in range(len(numbers)):
  ifTrue = True   
  for j in range(len(numbers[i][1])):
    string = str(numbers[i][1][j] * int(numbers[i][0]))
    for k in range(len(string)):
      if string[k] not in digits:
        ifTrue = False 
  for j in range(len(numbers[i][1])):
    if len(str(numbers[i][1][j] * numbers[i][0])) != 3:
      ifTrue = False
  product = (numbers[i][1][0] * 10) + numbers[i][1][1]
  productString = str(product * numbers[i][0])
  for j in range(len(productString)):
    if productString[j] not in digits:
      ifTrue = False
  if ifTrue == True:
    valids.append(numbers[i])
  else:
    continue

print(valids)

fout.write (str(len(valids)) + '\n')

fout.close()
