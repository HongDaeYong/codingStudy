def solution(n, time):
    time.sort()
    right = n * max(time)
    left = 1
    answer = 0
    while left <= right:
        mid = (right + left) // 2
        tot = 0
        for i in time:
            tot += mid // i
        if tot >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return answer


print(solution(6, [7, 10]))