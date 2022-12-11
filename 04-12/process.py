f = open('input.txt', 'r')

inputArray = []
elfContains = 0
elfOverlap = 0

for rawline in f:
    line = rawline.strip()
    elf1 = [0,0]
    elf2 = [0,0]
    split = line.split(",")
    rawElf1= split[0].split("-")
    rawElf2= split[1].split("-")
    elf1 = [int(rawElf1[0]),int(rawElf1[1])]
    elf2 = [int(rawElf2[0]),int(rawElf2[1])]
    inputArray.append([elf1,elf2])

count = 0
for pair in inputArray:
    elf1 = pair[0]
    elf2 = pair[1]
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        elfContains += 1
    elif elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        elfContains += 1

    if elf1[0] >= elf2[0] and elf1[0] <= elf2[1]:
        elfOverlap += 1
    elif elf1[1] >= elf2[0] and elf1[1] <= elf2[1]:
        elfOverlap += 1
    elif elf2[0] >= elf1[0] and elf2[0] <= elf1[1]:
        elfOverlap += 1
    elif elf2[1] >= elf1[0] and elf2[1] <= elf1[1]:
        elfOverlap += 1
    count += 1

print("Pairs containing each other:", elfContains)
print("Pairs overlapping each other:", elfOverlap)

