def solution(stock, dates, supplies, k):
    answer = 0
    dates.append(k)
    supplies.append(-1)
    timePast = []
    timePast.append(dates[0])
    date = 0
    max = -1
    takeIt = False
    for i in range(1,len(dates)):
        timePast.append(dates[i]-dates[i-1])
    for i, (tL, sup) in enumerate(zip(timePast, supplies)):
        stock -= tL
        date += timePast[i]
        if sup != -1 and stock - timePast[i+1] < 0:
            answer += 1
            stock += sup
        elif stock + sup - sum(timePast[i+1:]) >= 0:
            return answer
        else:
            for j in range(i+2, len(timePast)):
                if stock + sup - sum(timePast[i+1:j+1]) >= 0 and j > max:
                    max = j
                    takeIt = True
            if takeIt:
                stock += sup
                answer += 1
    return answer


stock, dates, supplies, k = 4, [4, 10, 15], [20, 5, 10], 30
stock2, dates2, supplies2, k2 = 1, [1,3,7,15], [10, 1,3,5], 4
print(solution(stock, dates, supplies, k))
print(solution(stock2, dates2, supplies2, k2))

