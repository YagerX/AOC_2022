from math import lcm
f = open('input.txt', 'r')
prompt = f.read().splitlines()

class monkey:
    def __init__(self):
        self.items = []
        self.operation = ""
        self.opAmount = 0
        self.test = 0
        self.tMonkey = -1
        self.fMonkey = -1
        self.inspections = 0
        
monkeyList = []
curMonk = 0

for line in prompt:
    instr = line.split()
    if len(instr) > 0:
        if instr[0] == 'Monkey':
            curMonk = int(instr[1][0])
            monkeyList.append(monkey())
        elif instr[0] == 'Starting':
            for x in range(2,len(instr)):
                monkeyList[curMonk].items.append(int(instr[x].strip(',')))
        elif instr[0] == 'Operation:':
            monkeyList[curMonk].operation = instr[4]
            monkeyList[curMonk].opAmount = instr[5]
        elif instr[0] == 'Test:':
            monkeyList[curMonk].test = int(instr[3])
        elif instr[1] == 'true:':
            monkeyList[curMonk].tMonkey = int(instr[5])
        elif instr[1] == 'false:':
            monkeyList[curMonk].fMonkey = int(instr[5])

divisors = []
for monkey in monkeyList:
    divisors.append(monkey.test)
    modulus = lcm(*divisors)
    print(monkey.items,monkey.operation,monkey.opAmount,monkey.test,monkey.tMonkey,monkey.fMonkey)            
    
curRound = 1

def cycleMonkey():
    for monkey in monkeyList:
        for x in range(len(monkey.items)):
            #Perform inspection for each item
            if monkey.operation == '+':
                if monkey.opAmount == 'old':
                    monkey.items[0] = monkey.items[x] * 2
                else:
                    monkey.items[0] += int(monkey.opAmount)
            if monkey.operation == '*':
                if monkey.opAmount == 'old':
                    monkey.items[0] = monkey.items[0] * monkey.items[0]
                else:
                    monkey.items[0] *= int(monkey.opAmount)
            monkey.inspections += 1
            #Reduce worry level by /3
            #monkey.items[0] = monkey.items[0]/3 //1
            monkey.items[0] = monkey.items[0] % modulus
            #Perform tests and move monkeys as per results
            if monkey.items[0] % monkey.test == 0:
                monkeyList[monkey.tMonkey].items.append(monkey.items.pop(0))
            else:
                monkeyList[monkey.fMonkey].items.append(monkey.items.pop(0))

for i in range(10000):
    cycleMonkey()
for monkey in monkeyList:
    print(monkey.inspections, monkey.items,monkey.operation,monkey.opAmount,monkey.test,monkey.tMonkey,monkey.fMonkey)            
