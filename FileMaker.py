import RandomMathQuestionGenerator as rmqg

addDict = {}
subDict = {}
subDict2 = {}
multDict = {}
divDict = {}

#10 ADDITION
for i in range(12):
    addDict.update(rmqg.generateAddition(1, 100, 1, 100))

#10 SUBTRACTION WITH WHOLE NUMBER SOLUTIONS
for i in range(12):
    subDict.update(rmqg.generateSubtractionPositive(1, 200))

#10 SUBTRATION WITH INTEGER SOLUTIONS
for i in range(12):
    subDict2.update(rmqg.generateSubtractionAll(1, 100, -200, 200))

#10 MULTIPLICATION
for i in range(12):
    multDict.update(rmqg.generateMultiplication(1, 12, 1, 12))

#10 DIVISION
for i in range(12):
    divDict.update(rmqg.generateDivision(1, 144))



#open mathProblems.txt or create mathProblems.txt if nonexistant and then wipe the file clean
f = open("mathProblems.txt", "w+")
f.truncate(0)

#write addition problems to mathProblems.txt
f.write("ADDITION PROBLEMS \r\n")
for add in addDict:
    f.write(add + "\r\n")

#write subtraction problems to mathProblems.txt
f.write("SUBTRACTION PROBLEMS \r\n")
for sub in subDict:
    f.write(sub + "\r\n")

#write advanced subtraction problems to mathProblems.txt
f.write("MORE SUBTRACTION PROBLEMS \r\n")
for sub2 in subDict2:
    f.write(sub2 + "\r\n")

#write multiplication problems to mathProblems.txt
f.write("MULTIPLICATION PROBLEMS \r\n")
for mult in multDict:
    f.write(mult + "\r\n")

#write division problems to mathProblems.txt
f.write("DIVISION PROBLEMS \r\n")
for div in divDict:
    f.write(div + "\r\n")

#close the file reader/writer
f.close()


#open mathSolutions.txt or create mathSolutions.txt if nonexistant and then wipe the file clean
f = open("mathSolutions.txt", "w+")
f.truncate(0)

#write addition solutions to mathSolutions.txt
f.write("ADDITION SOLUTIONS \r\n")
for add in addDict:
    f.write(add + " = " + str(addDict[add]) + "\r\n")

#write subtraction solutions to mathSolutions.txt
f.write("SUBTRACTION SOLUTIONS \r\n")
for sub in subDict:
    f.write(sub + " = " + str(subDict[sub]) + "\r\n")

#write advanced subtraction solutions to mathSolutions.txt
f.write("MORE SUBTRACTION SOLUTIONS \r\n")
for sub2 in subDict2:
    f.write(sub2 + " = " + str(subDict2[sub2]) + "\r\n")

#write multiplication solutions to mathSolutions.txt
f.write("MULTIPLICATION SOLUTIONS \r\n")
for mult in multDict:
    f.write(mult + " = " + str(multDict[mult]) + "\r\n")

#write division solutions to mathSolutions.txt
f.write("DIVISION SOLUTIONS \r\n")
for div in divDict:
    f.write(div + " = " + str(divDict[div]) + "\r\n")