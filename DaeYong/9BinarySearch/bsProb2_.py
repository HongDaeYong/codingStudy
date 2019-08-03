def solution(n, times):
    answer = 0
    validTimes = [0]
    for t in times:
        i = 1
        while t * i <= n * max(times):
            validTimes.append(t * i)
            i += 1
    validTimes = list(set(validTimes))
    validTimes.sort()
    print(validTimes)
    onWorking = [0 for _ in times]
    for t in validTimes:
        pass

    return answer


n = 6
times = [7, 10]
print(solution(n, times))

