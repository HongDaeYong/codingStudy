def solution(numbers, target):
    answer = 0
    pn=[0]
    for i in numbers:
        temporary=[]
        for j in pn:
            temporary.append(j+i)
            temporary.append(j-i)
        pn=temporary
    answer=pn.count(target)
    return answer