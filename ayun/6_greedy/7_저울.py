def solution(weight):
    answer = 0
    weight.sort()
    sum=1
    for i in range(len(weight)):
        if sum<weight[i]:
            return sum
        sum+=weight[i]
    return sum