
def checkDifferentLines(combList, ifTrue, i, loopList):
    for j in range(len(combList[i])):
        localList = []
        position = j
        localTrue = False
        while localTrue == False:
            localVariable = -1
            localIndex = None
            for k in range(len(combList[i])):
                if combList[i][position] == combList[i][k]:
                    continue
                else:
                    if combList[i][position][1] == combList[i][k][1] and combList[i][position][0] < combList[i][k][0]:
                        if localVariable > combList[i][k][0] - combList[i][position][0] or localVariable < 0:
                            localVariable = combList[i][k][0] - combList[i][position][0]
                            localIndex = k
            if localIndex == None:
                localTrue = True
                continue
            else:
                if localIndex % 2 == 1:
                    position = localIndex - 1
                else:
                    position = localIndex + 1
                    """
            print(position)
            print("j=", j, " i=", i, " localIndex=", localIndex)
            print("loopList", loopList)
            """
            if combList[i][localIndex] not in localList:
                localList.append(combList[i][localIndex])
            else:
                if combList[i] not in loopList:
                    loopList.append(combList[i])
                localTrue = True

