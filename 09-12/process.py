f = open('input.txt', 'r')

inputArray = []
head = knot(0,0)
tail = knot(0,0)
tailTrail = ["0,0"]
snake = []
snakeTrail = ["0,0"]

class knot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
for line in f:
    inputArray.append(line[0:-1].split())

def moveHead(move):
    direc=move[0]
    dist = int(move[1])
    for i in range(dist):
        if direc == "U":
            head.y += 1
        elif direc == "D":
            head.y -= 1
        elif direc == "L":
            head.x -= 1
        elif direc == "R":
            head.x += 1
        moveTail()

def moveTail():
    if tail.x == head.x and tail.y == head.y:
        return
    if tail.x < head.x -1:
        tail.x += 1
        tail.y = head.y
    elif tail.x > head.x +1:
        tail.x -= 1
        tail.y = head.y
    elif tail.y < head.y -1:
        tail.y += 1
        tail.x = head.x
    elif tail.y > head.y +1:
        tail.y -= 1
        tail.x = head.x
    tailPos = str(tail.x) + "," + str(tail.y)
    if tailTrail.count(tailPos) == 0:
        tailTrail.append(tailPos)

def initSnake():
    for i in range(10):
        snake.append(knot(0,0))
        
def moveSnake(move):
    direc=move[0]
    dist = int(move[1])
    for i in range(dist):
        if direc == "U":
            snake[0].y += 1
        elif direc == "D":
            snake[0].y -= 1
        elif direc == "L":
            snake[0].x -= 1
        elif direc == "R":
            snake[0].x += 1
        for x in range(9):
            moveSeg(snake[x], snake[x+1])
        snakePos = str(snake[9].x) + "," + str(snake[9].y)
        if snakeTrail.count(snakePos) == 0:
            snakeTrail.append(snakePos)

def moveSeg(parent,child):
    if child.x < parent.x -1:
        child.x += 1
        if child.y < parent.y:
            child.y += 1
        elif child. y > parent.y:
            child.y -= 1
    elif child.x > parent.x +1:
        child.x -= 1
        if child.y < parent.y:
            child.y += 1
        elif child. y > parent.y:
            child.y -= 1
    elif child.y < parent.y -1:
        child.y += 1
        if child.x < parent.x:
            child.x += 1
        elif child. x > parent.x:
            child.x -= 1
    elif child.y > parent.y +1:
        child.y -= 1
        if child.x < parent.x:
            child.x += 1
        elif child. x > parent.x:
            child.x -= 1
    return

for move in inputArray:
    moveHead(move)
print(len(tailTrail))

initSnake()
for move in inputArray:
    moveSnake(move)
print(len(snakeTrail))
