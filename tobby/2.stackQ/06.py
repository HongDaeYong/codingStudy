def solution(ps):
    a = []
    l=len(ps)
    for i in range(l):
        t = ps[i]
        ta = 0
        cur =i+1
        for j in range(cur,l):
            ta+=1
            if ps[j] < t :
                break
        a.append(ta)
    return a
