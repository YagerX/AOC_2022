f = open('input.txt', 'r')

inputString = ""

for line in f:
    inputString += line[0:-1]


def findSOP(signal):
    for x in range(len(signal)-3):
        byte = signal[x:x+4]
        if byte.count(byte[0]) == 1 and byte.count(byte[1]) == 1 and byte.count(byte[2]) == 1 and byte.count(byte[3]) == 1:
            print("Unique @", x)
            print("Answer is", x+4)
            break

def findSOM(signal):
    for x in range(len(signal)-13):
        byte = signal[x:x+14]
        isUnique = True
        for i in range(14):
            if byte.count(byte[i]) > 1:
                isUnique = False
        print(isUnique)
        if isUnique:
            print("Unique @", x)
            print("Answer is", x+14)
            break

findSOP(inputString)
findSOM(inputString)
