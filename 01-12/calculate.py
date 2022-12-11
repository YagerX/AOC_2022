f = open('input.txt', 'r')

inputArray = []
elfCalorie = [0]
curElf = 0

for line in f.readlines():
    inputArray.append(line)
    if line == "\n":
        curElf += 1
        elfCalorie.append(0)
    else:
        elfCalorie[curElf] += int(line)

sortedElves = sorted(elfCalorie)
print(len(inputArray))
print(curElf)

print(elfCalorie[0])
print(sortedElves[248] + sortedElves[247] + sortedElves[246])

