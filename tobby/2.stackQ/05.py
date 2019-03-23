def solution(hs):
    answer = []
    for i, v in enumerate(hs):
        t = 0
        for j in range(i-1,-1,-1):
            if(hs[j] > v):
                t = j+1
                break
        answer.append(t)
    return answer
