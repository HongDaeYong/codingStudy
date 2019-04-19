import itertools
def solution(number, k):
    answer = ''
    length=len(number)-k
    temp=[]
    for comb in itertools.combinations(range(len(number)),k):
        number2=number
        for i in comb:
            number2=number2.replace(number[i],"",1)
        temp.append(number2)
    return max(temp)