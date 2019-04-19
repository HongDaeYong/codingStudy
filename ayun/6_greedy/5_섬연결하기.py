def solution(n, costs):
    answer = 0
    visited=[]
    method=[]
    cost=0
    for j in range(len(costs)):
        for i in range(j,len(costs)):
            count=0
            if costs[i][0] not in visited:
                visited.append(costs[i][0])
                count+=1
            if costs[i][1] not in visited:
                visited.append(costs[i][1])
                count+=1
            if count>=1:
                cost+=costs[i][2]
        for i in range(0,j):
            if costs[i][0] not in visited:
                visited.append(costs[i][0])
                count+=1
            if costs[i][1] not in visited:
                visited.append(costs[i][1])
                count+=1
            if count>=1:
                cost+=costs[i][2]
        method.append(cost)
    return min(method)