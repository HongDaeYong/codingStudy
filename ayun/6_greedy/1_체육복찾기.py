def solution(n, lost, reserve):
    answer= n-len(lost)
    for i in reserve:
        if i-1 in lost:
            reserve.remove(i)
            answer+=1
    for i in reserve:
        if i+1 in lost:
            reserve.remove(i)
            answer+=1
    return answer