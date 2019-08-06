def solution(N, stages):
    failureRateList = []
    for i in range(0, N + 1):
        failureRateList.append([i, 0])
    challengerList = [ 0 for i in range(0, N + 2) ]
    sucessList = [ 0 for i in range(0, N + 1)]

    for s in stages:
        for i in range(1, s + 1):
            challengerList[i] += 1
        for i in range(1, s):
            sucessList[i] += 1

    for i in range(1, N + 1):
        if challengerList[i] is 0:
            failureRateList[i][1] = 0
            continue
        failureRateList[i][1] = (challengerList[i] - sucessList[i]) / challengerList[i]

    failureRateList.sort(key=lambda failureRateList: failureRateList[1], reverse=True)
    answer = []
    for e in failureRateList:
        if e[0] is 0:
            continue
        answer.append(e[0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3, 6, 6, 6, 5]))