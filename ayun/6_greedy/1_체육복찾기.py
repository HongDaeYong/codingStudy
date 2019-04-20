def solution(n, lost, reserve):
    answer= n-len(lost)+len(set(reserve)&set(lost))
    rreserve=set(reserve)-set(lost)
    llost=set(lost)-set(reserve)
    z=[]
    for i in rreserve:
        if i-1 in llost and i-1 not in z:
            z.append(i-1)
            answer+=1
        elif i+1 in llost and i+1 not in z:
            z.append(i+1)
            answer+=1
    return answer