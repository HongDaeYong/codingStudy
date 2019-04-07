def solution(n, lost, reserve):
    answer = n - len(lost) +len(set(reserve) & set(lost))
    a = []
    newReserve = set(reserve)- set(lost)
    newLost = set(lost) - set(reserve)
    for l in newLost:
        if l-1 in newReserve and l-1 not in a:
            a.append(l-1)
        elif l+1 in newReserve and l+1 not in a:
            a.append(l+1)

    return answer + len(a)
