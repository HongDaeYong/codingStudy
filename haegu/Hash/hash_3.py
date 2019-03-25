#[해쉬3번]위장
import collections
from functools import reduce
def solution(clothes):
    answer = 0
    mul_ =1
    sum_ =0
    closet={}
    for i in clothes:
        if i[1] in closet:
            closet[i[1]]+=1
        else:
            closet[i[1]] = 1
    print(closet)
    if len(closet.values())==1:
        for i in closet:
            return closet[i]
    else:
        for i in closet:
            closet[i]+=1
        return reduce(lambda x,y:x*y,closet.values())-1
