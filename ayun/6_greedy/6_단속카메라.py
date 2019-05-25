def solution(routes):
    answer = 0
    rr=[]
    rr.append([routes[0][0],routes[0][1]])
    for i in routes:
        for j in rr:
            if (j[0]<=i[0]<=j[1])or(j[0]<=i[1]<=j[1]):
                rr.append([i[0],i[1]])
            else:
                answer+=1
    return answer