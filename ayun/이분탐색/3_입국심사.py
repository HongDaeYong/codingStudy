def solution(n, times):
    answer = 0
    low=0
    high=n*max(times)
    while True:
        sim=0
        mid=(low+high)/2
        print(mid,low,high)
        for i in times:
            sim+=int(mid/i)
        print(sim)
        if sim>n:
            high=mid
        elif sim<n:
            low=mid
        else:
            return int(mid)