f = open('input.txt', 'r')

inputArray = []
width = 0
height = 0

for line in f:
    inputArray.append(line[0:-1])

width = len(inputArray[0])
height = len(inputArray)

def checkWest(x,y):
    treeValue = inputArray[y][x]
    for i in range(x):
        if inputArray[y][i] >= treeValue:
            return False
    return True

def checkEast(x,y):
    treeValue = inputArray[y][x]
    for i in range(x+1,width):
        if inputArray[y][i] >= treeValue:
            return False
    return True
    
def checkNorth(x,y):
    treeValue = inputArray[y][x]
    for i in range(y):
        if inputArray[i][x] >= treeValue:
            return False
    return True

def checkSouth(x,y):
    treeValue = inputArray[y][x]
    for i in range(y+1, height):
        if inputArray[i][x] >= treeValue:
            return False
    return True

def checkTree(x,y):
    if checkNorth(x,y) or checkSouth(x,y) or checkWest(x,y) or checkEast(x,y):
        return True
    else:
        return False

def findVisible():
    visibleTotal=0

    for x in range(1,width-1):
        for y in range(1, height-1):
            #print(x,y,checkTree(x,y))
            if checkTree(x,y):
                visibleTotal += 1

    print(visibleTotal + 99 + 99 + 97 + 97)

def visibleWest(x,y):
    score = 0
    treeValue = inputArray[y][x]
    for i in reversed(range(x)):
        if inputArray[y][i] < treeValue:
            score += 1
        else:
            score += 1
            return score
    return score

def visibleEast(x,y):
    score = 0
    treeValue = inputArray[y][x]
    for i in range(x+1,width):
        if inputArray[y][i] < treeValue:
            score += 1
        else:
            score += 1
            return score
    return score
    
def visibleNorth(x,y):
    score = 0
    treeValue = inputArray[y][x]
    for i in reversed(range(y)):
        if inputArray[i][x] < treeValue:
            score += 1
        else:
            score +=1
            return score
    return score

def visibleSouth(x,y):
    score = 0
    treeValue = inputArray[y][x]
    for i in range(y+1, height):
        if inputArray[i][x] < treeValue:
            score += 1
        else:
            score += 1
            return score
    return score

def visibleTree(x,y):
    return visibleEast(x,y) * visibleWest(x,y) * visibleNorth(x,y) * visibleSouth(x,y)

def findMaxVisible():
    maxScore = 0
    for x in range(width):
        for y in range(height):
            score = visibleTree(x,y)
            if score > maxScore:
                maxScore = score
    print(maxScore)
#findVisible()
findMaxVisible()
