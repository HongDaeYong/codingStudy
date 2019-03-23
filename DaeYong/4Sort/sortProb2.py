class number:
    def __init__(self, n):
        self.n = n
        self.originalZeros = 0
        self.tmpNum = n
        while int(self.tmpNum / 1000) == 0:
            self.tmpNum *= 10
            self.originalZeros += 1

    def getN(self):
        return self.n

    def getTmpNum(self):
        return self.tmpNum

    def getOriginalZeors(self):
        return self.originalZeros

    def getMaxDigit(self):
        return int(self.tmpNum / 1000)

    def getSecDigit(self):
        return int(self.tmpNum / 100)


def solution(numbers):
    answer = ''
    numDict = {i: [] for i in range(1, 10)}
    for num in numbers:
        numberClass = number(num)
        numDict[numberClass.getMaxDigit()].append(numberClass)
    for i in range(9, 0, -1):
        numDict[i].sort(key=number.getSecDigit, reverse=True)
        tmpList = []
        # for numberClass in numDict[i]:
        #     if numberClass.
        numDict[i].sort(key=number.getOriginalZeors, reverse=True)
        for numberClass in numDict[i]:
            answer += str(numberClass.getN())
    return answer

numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers1))
print(solution(numbers2))

