import itertools as it


def solution(baseball):
    numbers = [str(i) for i in range(1, 10)]
    cases = list(map(''.join, it.permutations(numbers, 3)))
    caseCheck = [1 for _ in range(len(cases))]
    for bball in baseball:
        target = str(bball[0])
        numStrike = bball[1]
        numBall = bball[2]

        for i, case in enumerate(cases):
            if caseCheck[i] == 1:
                tmpNumStrike = 0
                tmpNumBall = 0
                for j, t in enumerate(target):
                    if target[j] == case[j]:
                        tmpNumStrike += 1
                    elif t in case:
                        tmpNumBall += 1
                if tmpNumStrike != numStrike or tmpNumBall != numBall:
                    caseCheck[i] = 0
    return sum(caseCheck)


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
print(solution(baseball))

