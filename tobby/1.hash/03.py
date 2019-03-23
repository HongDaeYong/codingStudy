def solution(clothes):
    answer = 1 
    d = {}
    
    for cloth in clothes : 
        if cloth[1] not in d.keys():
            d[cloth[1]] = 2
        else :
            d[cloth[1]] +=1
    
    for n in d.values():
        answer *= n
    
    return answer - 1
