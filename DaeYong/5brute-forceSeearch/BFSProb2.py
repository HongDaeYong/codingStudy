import itertools


def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numNum = len(numbers)
    numbers = list(numbers)

    allPermut=[]
    for i in range(1, numNum+1):
        permut = list(map(''.join, itertools.permutations(numbers, i)))
        for p in permut:
            allPermut.append(int(p))
    allPermut = set(allPermut)
    for num in allPermut:
        if isPrime(num):
            answer += 1
    return answer


numbers1 = '17'
numbers2 = '011'
print(solution(numbers1))
print(solution(numbers2))

