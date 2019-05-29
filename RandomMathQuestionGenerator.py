import random

#GENERATE RANDOM ADDITION PROBLEM
def generateAddition (firstMin, firstMax, secondMin, secondMax):
    #randomly generate first and second numbers
    firstNum = random.randint(firstMin, firstMax + 1)
    secondNum = random.randint(secondMin, secondMax + 1)

    #create question and solution
    question = str(firstNum) + " + " + str(secondNum)
    solution = firstNum + secondNum

    #add them to dictionary
    addDict = {
        question : solution
    }

    return addDict

#GENERATE RANDOM SUBTRACTION PROBLEM WHERE SOLUTION IS POSITIVE
def generateSubtractionPositive (firstMin, firstMax):
    firstNum = random.randint(firstMin, firstMax + 1)
    secondNum = random.randint(0, firstNum + 1)

    question = str(firstNum) + " - " + str(secondNum)
    solution = firstNum - secondNum

    subDict = {
        question: solution
    }

    return subDict

#GENERATE RANDOM SUBTRACTION PROLEM WHERE SOLUTION CAN BE POSITIVE OR NEGATIVE
def generateSubtractionAll(firstMin, firstMax, secondMin, secondMax):
    firstNum = random.randint(firstMin, firstMax + 1)
    secondNum = random.randint(secondMin, secondMax + 1)

    question = str(firstNum) + " - " + str(secondNum)
    solution = firstNum - secondNum

    subDict = {
        question: solution
    }

    return subDict

#GENERATE RANDOM MULTIPLICATION PROBLEM
def generateMultiplication(firstMin, firstMax, secondMin, secondMax):
    firstNum = random.randint(firstMin, firstMax + 1)
    secondNum = random.randint(secondMin, secondMax + 1)

    question = str(firstNum) + " x " + str(secondNum)
    solution = firstNum * secondNum

    multDict = {
        question: solution
    }

    return multDict

#GENERATE RANDOM DIVISION PROBLEM WITH SOLUTION BEING AN INTEGER
def generateDivision(firstMin, firstMax):
    firstNum = random.randint(firstMin, firstMax + 1)

    factors = [1]
    for c in range(1, firstNum + 1):
        if firstNum % c == 0:
            factors.extend([c])

    secondNum = random.choice(factors)

    question = str(firstNum) + " / " + str(secondNum)
    solution = firstNum / secondNum

    divDict = {
        question : solution
    }

    return divDict

#qaDict = {}
#qaDict.update(generateAddition(0, 10, 0, 10))
#qaDict.update(generateSubtractionPositive(0, 10))
#qaDict.update(generateSubtractionAll(0, 10, 10, 20))
#qaDict.update(generateMultiplication(0, 12, 0, 12))
#qaDict.update(generateDivision(1, 108))
#print(qaDict)

