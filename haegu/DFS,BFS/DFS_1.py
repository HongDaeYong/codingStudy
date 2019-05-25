import itertools
def solution(numbers, target):
    answer = 0
    num = list(map(str, numbers))
    print(num)
    for i in list(itertools.product(['-', '+'], repeat=len(numbers))):
        sum_ = 0
        for j in zip(i, num):
            sum_ += int(j[0] + j[1])
        if sum_ == target:
            answer += 1

    return answer