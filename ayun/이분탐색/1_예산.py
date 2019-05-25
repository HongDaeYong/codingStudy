def solution(budgets, M):
    answer = 0
    # budgets.sort()
    low=0
    high=max(budgets)
    while True:
        sum=0
        mid=(low+high)/2
        for i in budgets:
            if i > mid:
                sum+=mid
            else:
                sum+=i
        print(sum)
        if sum==M:
            return mid
        elif sum<M:
            low=mid
        elif sum>M:
            high=mid
solution([120,110,140,150],485)