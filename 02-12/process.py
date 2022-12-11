f = open('input.txt', 'r')

inputArray = []
scoreTally = 0


#for line in f.readlines():
#    inputArray.append(line)
#    if (line[0] == "A"):
#        if(line[2] == "X"):
#            scoreTally += (1 + 3)
#        if(line[2] == "Y"):
#            scoreTally += (2 + 6)
#        if(line[2] == "Z"):
#            scoreTally += (3 + 0)
#
#    elif(line[0] == "B"):
#        if(line[2] == "X"):
#            scoreTally += (1 + 0)
#        if(line[2] == "Y"):
#            scoreTally += (2 + 3)
#        if(line[2] == "Z"):
#            scoreTally += (3 + 6)
#    elif(line[0] =="C"):
#        if(line[2] == "X"):
#            scoreTally += (1 + 6)
#        if(line[2] == "Y"):
#            scoreTally += (2 + 0)
#        if(line[2] == "Z"):
#            scoreTally += (3 + 3)
            
for line in f.readlines():
    inputArray.append(line)
    if (line[0] == "A"):
        if(line[2] == "X"):
            scoreTally += (0 + 3)
        if(line[2] == "Y"):
            scoreTally += (3 + 1)
        if(line[2] == "Z"):
            scoreTally += (6 + 2)

    elif(line[0] == "B"):
        if(line[2] == "X"):
            scoreTally += (0 + 1)
        if(line[2] == "Y"):
            scoreTally += (3 + 2)
        if(line[2] == "Z"):
            scoreTally += (6 + 3)
    elif(line[0] =="C"):
        if(line[2] == "X"):
            scoreTally += (0 + 2)
        if(line[2] == "Y"):
            scoreTally += (3 + 3)
        if(line[2] == "Z"):
            scoreTally += (6 + 1)
print(scoreTally)
