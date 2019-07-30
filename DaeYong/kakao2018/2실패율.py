def solution(N, stages):
    answer = []
    notClear = [0 for _ in range(N)]
    numPlayer = [0 for _ in range(N)]
    for stage in stages:
        if stage != N + 1:
            notClear[stage-1] += 1
        for previousStage in range(stage):
            if previousStage != N:
                numPlayer[previousStage] += 1
    fail_rate = [[i, nC/nP] if nP != 0 else [i, 0] for i, (nC, nP) in enumerate(zip(notClear, numPlayer))]
    fail_rate.sort(key=lambda x: x[1], reverse=True)
    for fr in fail_rate:
        answer.append(fr[0]+1)
    return answer


inputs = [(5, [2, 1, 2, 6, 2, 4, 3, 3]), (4, [4, 4, 4, 4, 4])]
for inpt in inputs:
    print(solution(*inpt))

