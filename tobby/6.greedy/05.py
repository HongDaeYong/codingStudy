def solution(routes):
    answer = 1
    routes.sort()
    m = 30001
    
    for r in routes :
        if r[0] > m :
            answer += 1
            m = r[1]
        
        if r[1] < m :
            m = r[1]
        
    return answer