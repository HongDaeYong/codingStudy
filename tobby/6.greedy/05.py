def solution(n, costs):
    answer = 0
    islands = [0]
    
    for i in range(n-1):
        a = 0
        min_ = 99999999; 
        for cost in costs :
            if (cost[0] in islands) and (cost[1] not in islands) :
                if cost[2] < min_ :
                    a = cost[1]
                    min_ = cost[2]
            elif (cost[1] in islands) and (cost[0] not in islands) :
                if cost[2] < min_ :
                    a = cost[0]
                    min_ = cost[2]
        islands.append(a)
        answer += min_   
    return answer
