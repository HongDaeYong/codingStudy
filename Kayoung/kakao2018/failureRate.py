def solution(N, stages):
    answer = []
    answerList = []
    for i in range(1, N+1):
        answerList.append([i, 0])

    stages.sort()
    print(stages)
    watchingStage = stages[0]
    failCnt = 0
    prevFailCnt = 0
    challengerTot = len(stages)
    for s in stages:
        if s <= watchingStage:
            failCnt += 1
            continue
        challengerTot -= prevFailCnt
        failRate = failCnt / challengerTot
        answerList[watchingStage - 1][1] = failRate
        prevFailCnt = failCnt
        failCnt = 1
        watchingStage = s




    # challengerTot -= prevFailCnt
    # answerList[N-1][1] = failCnt / challengerTot
    answerList.sort(key=lambda answerList: answerList[1], reverse=True)
    print(answerList)
    for a in answerList:
        answer.append(a[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))