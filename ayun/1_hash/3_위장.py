def solution(clothes):
    answer = 0
    kind=[]
    dic={}
    a=1
    for i in range(len(clothes)):
        kind.append(clothes[i][1])
    for val in kind:
        if val not in dic:
            dic[val]=1
        else:
            dic[val]=dic[val]+1
    for i in dic.values():
        a=a*(i+1)
    return a-1