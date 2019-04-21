# 90 점
# def solution(budgets, M):
#     if sum(budgets) <= M:
#         return max(budgets)
#     else:
#         LUB = max(budgets)
#         rejectedAmount = 0
#         while rejectedAmount < sum(budgets) - M:
#             LUB -= 1
#             rejectedAmount = sum([budget - LUB if budget >= LUB else 0 for budget in budgets])
#         return LUB


def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)
    else:
        upper = max(budgets)
        lower = 0
        previousLUB = None
        while True:
            LUB = int((upper + lower) / 2)
            if previousLUB == LUB:
                break
            previousLUB = LUB
            rejectedAmount = sum([budget - LUB if budget >= LUB else 0 for budget in budgets])
            if rejectedAmount >= sum(budgets) - M:
                lower = LUB
            else:
                upper = LUB
        return previousLUB


input = ([120, 110, 140, 150], 485)
print(solution(*input))

