def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)
    upper = max(budgets)
    lower = 0
    while upper-lower > 1:
        LUB = int((upper + lower) / 2 )
        a = sum([budget-LUB if budget >= LUB else 0 for budget in budgets])
        if a>=sum(budgets) - M:
            lower =LUB
        else : 
            upper = LUB
    return int((upper + lower) / 2 )