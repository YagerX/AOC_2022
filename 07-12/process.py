f = open('input.txt', 'r')

inputArray = []
fileTree = []
dirSums = 0
dirList = []

for line in f:
    inputArray.append(line[0:-1])
 
class direc:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subDirecs = []
        self.files = []
        self.fileSize = 0
        self.netSize = ""

    def getSubDirs(self):
        outputStr = ""
        for x in self.subDirecs:
            outputStr += x.name
            outputStr += ", "
        return outputStr[0:-2]

    def getFiles(self):
        outputStr = ""
        for x in self.files:
            outputStr += x.name
            outputStr += ", "
        return outputStr[0:-2]

    def findDir(self,dirName):
        if dirName == "..":
            if self.parent != None:
                return self.parent
            else:
                return self
        for x in self.subDirecs:
            if x.name == dirName:
                return x
            
    def updateFS(self):
        folderSize = 0
        fileSize = 0
        for folder in self.subDirecs:
            folderSize += folder.netSize
        for f in self.files:
            fileSize += f.size
        self.fileSize = fileSize
        self.netSize = fileSize + folderSize

class datum:
    def __init__(self,name,size):
        self.name = name
        self.size = int(size)

def doNothing():
    return

def runComs(inputComs, num, rootDir):
    inputComs.pop(0)
    curDir = rootDir
    for index in range(num):
        command = inputComs[index].split()
#        print(command)
        if command[0] == "$" and command[1] == "cd":
#            print("    Moving working directory to", command[2])
            if command[2] == "..":
                curDir.updateFS()
            curDir = curDir.findDir(command[2])
#            print("    Working directory is now", curDir.name)
        elif command[0] == "$" and command[1] == "ls":
#            print("    Listing current folder's contents")
#            print(curDir.getSubDirs())
            doNothing()
        elif command[0] == "dir":
#            print("    Making new Dir called:", command[1])
            newDirec = direc(command[1], curDir)
            curDir.subDirecs.append(newDirec)
#            print("        Current Directory:", curDir.name,  curDir, "now has subdirectories", curDir.getSubDirs())
        else:
#            print("    Making new file called:", command[1], "size:", command[0])
            curDir.files.append(datum(command[1],command[0]))
            curDir.fileSize += int(command[0])
#            print("    Current directory has files:", curDir.getFiles(), "current directory's files total size:", curDir.fileSize)


def printDirTree(direc, indents):
    outputString = ""
    outputIndent = indents*" "
    outputString += direc.name + "\n"
    for x in direc.subDirecs:
        printDirTree(x, indents + 1)
    direc.updateFS()
    global dirSums
    global dirList
    dirList.append(direc.netSize)
    if direc.netSize <= 100000:
        dirSums += direc.netSize

rootDir = direc("/", None)
runComs(inputArray, len(inputArray)-1, rootDir)
printDirTree(rootDir, 0)
print(dirSums)
dirList.sort()
print(dirList)
