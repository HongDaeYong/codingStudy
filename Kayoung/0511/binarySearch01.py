def solution(budgets, M):
    budgets.sort()
    head = budgets[0]
    tail = budgets[-1]
    answer = 0
    while True:
        mid = int((head + tail) / 2)
        sum = calculateSum(budgets, mid)
        if sum > M:
            tail = mid
        else:
            head = mid
            while True:
                mid = int((head + tail) / 2)
                sum = calculateSum(budgets, mid)
                if sum < M:
                    head = mid
                elif sum == M:
                    return mid
                else:
                    i = tail
                    while i >= head:
                        sum = calculateSum(budgets, i)
                        if sum < M:
                            answer = i
                            break
                        i -= 1
                    return answer

def calculateSum(budgets, limit):
    sum = 0
    for i in budgets:
        if i > limit:
            sum += limit
        else:
            sum += i
    return sum

print(solution([120, 110, 140, 150], 485))