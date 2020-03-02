with open('e_so_many_books.txt', 'r') as file:
    line1 = file.readline()
    numBooks, numLib, deadline = int(line1.split()[0]), int(line1.split()[1]), int(line1.split()[2])
    line2 = file.readline()
    scoreList = [int(n) for n in line2.split()]
    libData = [[]]*numLib
    libBookList = [[]]*numLib
    for libIndex in range(numLib):
        firstLine = file.readline()
        libData[libIndex] = [int(n) for n in firstLine.split()]
        #Contains no. of books in library, signup time and books/day in order as an array
        #libData itself is an array of arrays, each index represents a library
        secondLine = file.readline()
        libBookList[libIndex] = [int(n) for n in secondLine.split()]
        #libBookList is also an array of arrays
        #each sub-array is the list of indexes of the books in the library of the main index (think of as 2D array)

decisionScoreList = [0]*numLib
p = 0.75  # factor that we can vary for different results
for i in range(numLib):
    netScore=0
    for j in range(libData[i][0]):
        netScore += scoreList[libBookList[i][j]]
    decisionScoreList[i] = netScore*libData[i][2]/(libData[i][0]*pow(libData[i][1], p))

finalLibOrder = [index for index, value in sorted(enumerate(decisionScoreList), reverse=True, key=lambda x: x[1])]

with open('partEResult.txt', 'w+') as file:
    outputStringList = [str(numLib)+'\n']
    for i in range(numLib):
        index = finalLibOrder[i]
        str1 = ' '.join([str(index), str(libData[index][0])])+'\n'
        outputStringList.append(str1)
        str2 = ' '.join([str(n) for n in libBookList[index]])+'\n'
        outputStringList.append(str2)
    file.writelines(outputStringList)

print(finalLibOrder)
