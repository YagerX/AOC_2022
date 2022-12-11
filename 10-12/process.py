f = open('input.txt', 'r')

inputArray = []
signalCheck = [20,60,100,140,180,220]
curCycle = 0
regX = 1
signalSum = 0
registerRecord = []

for line in f:
    inputArray.append(line[0:-1].split())

def checkMarker(tick):
    if signalCheck.count(tick) == 1:
        global signalSum
        signalSum += tick*regX
    
    
for instr in inputArray:
    registerRecord.append(regX)
    curCycle += 1
    checkMarker(curCycle)
    if instr[0] == 'addx':
        registerRecord.append(regX)
        curCycle += 1
        checkMarker(curCycle)
        regX += int(instr[1])
print(signalSum)

buffStr = ''
for i in range(240):
    row = int(i/40)//1
    col = i-row*40
    reg = registerRecord[i]
    if reg == col or reg == col-1 or reg == col+1:
        buffStr += "█"
    else:
        buffStr += " "
    if col == 39:
        buffStr += "\n"
print(buffStr)
