with open('b_read_on.txt', 'r') as file:
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

# for part b, each library is completely unique, processes 1 book at a time and all books are worth 100.
# we just need to optimize order based on sign up time

signDaysList = []
for i in range(numLib):
    signDaysList.append(libData[i][1])

finalLibOrder = [index for index, value in sorted(enumerate(signDaysList), reverse=False, key=lambda x: x[1])]

with open('partBResult.txt', 'w+') as file:
    outputStringList = [str(numLib)+'\n']
    for i in range(numLib):
        index = finalLibOrder[i]
        str1 = ' '.join([str(index), str(libData[index][0])])+'\n'
        outputStringList.append(str1)
        str2 = ' '.join([str(n) for n in libBookList[index]])+'\n'
        outputStringList.append(str2)
    file.writelines(outputStringList)

print(finalLibOrder)
