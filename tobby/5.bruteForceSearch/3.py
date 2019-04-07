def solution(baseball):
    answer = []
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if i!=j and j!=k and i!=k:
                    answer.append("{}{}{}".format(i,j,k))           
    for a in baseball:
        temp =[]
        for n in answer :
            ts = 0
            tb = 0
            for i in range(3):
                for j in range(3):
                    if str(a[0])[i] == n[j]:
                        if i==j:
                            ts +=1
                        else :
                            tb +=1            
            if ts == a[1] and tb == a[2]:
                temp.append(n)        
        answer = temp
    return len(answer)
