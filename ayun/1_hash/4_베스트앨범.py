def solution(genres, plays):
    answer = []
    rr=[]
    g=set(genres)
    p=list(zip(genres,plays))
    for i in g:
        s=0
        for j in p:
            if j[0]==i:
                s=s+j[1]
        answer.append(s)
    ge=list(zip(g,answer))
    ge.sort(key=lambda s:s[1],reverse=True)
    for i in ge:
        song=[]
        for j in p:
            if i[0]==j[0]:
                song.append(j[1])
                song.sort(reverse=True)
        if len(song)==1:
            rr.append(plays.index(song[0]))
        else:
            rr.append(plays.index(song[0]))
            rr.append(plays.index(song[1]))
    return rr