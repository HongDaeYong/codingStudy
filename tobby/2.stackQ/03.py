def solution(bl, w, tws):
    a = 1
    b =[]
    
    while len(b) or len(tws):    
        if len(tws) and sum(b)+tws[0] <= w :
            b.append([tws.pop(0),0])
        
        for i in range(len(b)):
            b[i][1] += 1
        
        if len(b) and b[0][1]==bl:
            b.pop(0)
    
        a += 1
    
    return a
