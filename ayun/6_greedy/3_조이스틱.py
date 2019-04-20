def solution(name):
    answer = 0
    now="A"*len(name)
    now2=now
    i=0
    while True:
        if now2==name:
            return answer
        if name[i]>="A" and name[i]<="M":
            now2.replace(now[i],name[i],1)
            answer+=(ord(name[i])-ord("A"))
        else:
            now2.replace(now[i],name[i],1)
            answer+=(91-ord(name[i]))
        if i!=len(name)-1:
            if name[i+1]=='A':
                i=i-1
                answer+=1
                if i<0:
                    i=i+len(name)
            else:
                answer+=1
                i+=1
        answer+=1
    return answer-1