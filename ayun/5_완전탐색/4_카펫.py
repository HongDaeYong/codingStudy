def solution(brown, red):
    answer = []
    total=brown+red
    r = list()
    for i in range(1, red+1):
        if (red%i) == 0 :
            r.append(i)
    for i in r[::-1]:
        red/i
        a=1
        if total%(i+2*a)==0:
            if red/i+2==total/(i+2*a):
                return [i+2*a,int(total/(i+2*a))]
        a=a+1
        if total%(i+2*a)==0:
            if red/i+2==total/(i+2*a):
                return [i+2*a,int(total/(i+2*a))]