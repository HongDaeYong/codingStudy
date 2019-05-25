def solution(budgets, M):
    budgets.sort()
    head = budgets[0]
    tail = budgets[-1]

    #상한선 조절
    while True:
        mid = int((head + tail) / 2)
        sum = calculateSum(budgets, mid)
        if sum > M:
            tail = mid
        else:
            head = mid
            break

    #하한선 조절
    while True:
        mid = int((head + tail) / 2)
        sum = calculateSum(budgets, mid)
        if sum < M:
            head = mid
        elif sum == M:
            return mid
        else:
            break
    i = tail
    while i >= head:
        if calculateSum(budgets, i) <= M:
            return i
        i -= 1

def calculateSum(budgets, limit):
    sum = 0
    for i in budgets:
        if i > limit:
            sum += limit
        else:
            sum += i
    return sum

print(solution([120, 110, 140, 150], 485))