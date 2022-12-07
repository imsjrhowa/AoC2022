d = {}

mainDirectory = dd

line = ""
currentDir = ''

line = data.pop(0)
while data:
    if line[0] == '$':
        if contains(line, "ls"):
            line = data.pop(0)
            while( contains(line,"$") == False ):                
                line = line.split(' ')
                if contains(line,"dir"):
                    print(currentDir, line)                                
                    d[currentDir].append(line[1])
                else:
                    print(currentDir, "file:", line)                                
                    d[currentDir].append(line)        

                if len(data):
                    line = data.pop(0)
                else:
                    break;

        elif contains(line, "cd"):
            line = line.split(' ')
            if line[2] == '/':
                print("Root")
                currentDir = '/'
                d[currentDir] = []
            elif line[2] == '..':
                print("..")
                prev = d[currentDir][0]
                if prev[0] != "prev":
                    print("ERROR")
                currentDir = prev[1]
            else:
                print("cd ", line[2])
                prevDirectory = currentDir
                currentDir = line[2]
                if currentDir in d:
                    print("ERROR")
                d[currentDir] = [["prev",prevDirectory]]

            line = data.pop(0)

def calcDirectorySize( str ):
    size = 0
    for i in range( len(str) ):
        if isinstance(str[i], list):
            if str[i][0] != "prev":
                size += (int)(str[i][0])
        elif len(str[i]) > 0:              
            if str[i] in d:
                size += calcDirectorySize(d[str[i]])
    return size

dirSizes = {}
for directory in d:
    if directory == '/':
        continue

    line = d[directory]
    size = 0

    size += calcDirectorySize( line )

    if size < 100000:                
        dirSizes[directory] = size

print(dirSizes)

totalSize = 0
for s in dirSizes:
    totalSize += dirSizes[s]

print("Answer ", totalSize)
