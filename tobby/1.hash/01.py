from collections import Counter

def solution(pt, cn):
    r=Counter(pt+cn)
    
    for k in r:
        if r[k]%2==1:
            return k
