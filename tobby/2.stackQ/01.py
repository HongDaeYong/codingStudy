def solution(ar):
    an = 0
    n = 0
    for i,a in enumerate(ar):
        if a=='(':
            if ar[i+1]==')':
                an += n
            else:
                n += 1
                an += 1
        elif ar[i-1]!='(':
            n -=1
                
    return an
