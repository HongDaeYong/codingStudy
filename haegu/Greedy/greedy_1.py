#1 탐욕법 체육복

def solution(n, lost, reserve):
    answer = n
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for i in range(1, n + 1):
        if i in lost:
            if i + 1 in reserve:
                reserve.remove(i + 1)
            elif i - 1 in reserve:
                reserve.remove(i - 1)
            else:
                answer -= 1

    return answer