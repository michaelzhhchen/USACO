"""
ID: michael332
LANG: PYTHON3
TASK: milk2
"""
fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
Num = int(fin.readline())
theInput = []
for i in range(Num):
    first, last = list(map(int, fin.readline().split()))
    theInput.append([first, last])

theInput.sort()
maxMilk = 0
maxGap = 0
beginningSequence = 0
endingSequence = 0

print("TheInput: ", theInput)
for i in range(len(theInput)):
    if i == 0:
        beginningSequence = theInput[i][0]
        endingSequence = theInput[i][1]
    else:
        if theInput[i][0] <= endingSequence:
            if theInput[i][1] > endingSequence:
                endingSequence = theInput[i][1]
        else:
            if maxGap < theInput[i][0] - endingSequence:
                maxGap = theInput[i][0] - endingSequence
            if maxMilk < endingSequence - beginningSequence:
                maxMilk = endingSequence - beginningSequence
            beginningSequence = theInput[i][0]
            endingSequence = theInput[i][1]
    print("Beg: ", beginningSequence)
    print("End: ", endingSequence)
    print("MaxM: ", maxMilk)
    print("MaxG: ", maxGap)

if maxMilk < endingSequence - beginningSequence:
    maxMilk = endingSequence - beginningSequence

fout.write (str(maxMilk) + ' ' + str(maxGap) + '\n')
fout.close()
