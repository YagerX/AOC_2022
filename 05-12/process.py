f = open('input.txt', 'r')

inputArray = []
boxStack = []
moveList=[]
initialHeight = 8

for line in f:
    inputArray.append(line[0:-1])


def generateStack():
    for x in range(9):
        boxStack.append([])
    for x in range(initialHeight):
        for y in range(9):
            if inputArray[initialHeight-x-1][y*4 + 1] != ' ':
                boxStack[y].append(inputArray[initialHeight-x-1][y*4 + 1])

def generateMoveList():
    for x in range(10, len(inputArray)):
        moveList.append(inputArray[x].split()[1::2])

def printStack():
    maxLen = 0
    stackStr = []
    for x in range(9):
        if len(boxStack[x]) > maxLen:
            maxLen = len(boxStack[x])
    for y in range(maxLen):
        line = ""
        for z in range(9):
            if y < len(boxStack[z]):
                line += boxStack[z][y]
            else:
                line += " "
        stackStr.append(line)
    for i in range(len(stackStr)):
        print(stackStr.pop())
    print("123456789")

def moveCrates(move):
    moves = int(move[0])
    origin = int(move[1])-1
    dest = int(move[2])-1
    for x in range(moves):
        boxStack[dest].append(boxStack[origin].pop())

def altMove(move):
    moves = int(move[0])
    origin = int(move[1])-1
    dest = int(move[2])-1
    tempStack = []
    for x in range(moves):
        tempStack.append(boxStack[origin].pop())
    for x in range(moves):
        boxStack[dest].append(tempStack.pop())

def printTopCrates():
    outputStr = ""
    for x in range(9):
        topBox = len(boxStack[x])
        outputStr += boxStack[x][topBox-1]
    return outputStr

def ogPerformMoves():
    for x in moveList:
        moveCrates(x)
    printStack()
    print("Top boxes:", printTopCrates())

def altPerformMoves():
    for x in moveList:
        altMove(x)
    printStack()
    print("Top boxes:", printTopCrates())

    
generateStack()
generateMoveList()

altPerformMoves()
