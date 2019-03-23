def solution(genres, plays):
    an = []
    sg = set(genres)
    d = {g : [(0,-1),(0,-1)] for g in sg}
    dn = {g : 0 for g in sg}

    for i,p in enumerate(plays):
        tg = genres[i]
        dn[tg] += p
        if p >  d[tg][1][0]:
            d[tg][1] = (p,i)
            d[tg].sort(reverse=True , key = lambda a : a[0])
    
    t = [w for w in d.values()]
    
    t.sort(reverse = True, key = lambda a : dn[genres[a[0][1]]] )
    
    for ta in t : 
        for w in ta:
            if w[1] != -1:
                an.append(w[1])
    
    return an
