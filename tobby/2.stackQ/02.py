def solution(p, l):
    answer = 0

    while True:
        t = p.pop(0)
        if len(p) != 0 and t < max(p):
            p.append(t)
            if l==0:
                l=len(p)
        else:
            answer +=1
            if l==0:
                return answer

        l -=1
    return answer
