# 저울
def solution(weight):
    answer = 0
    weight.sort()
    sum = weight.pop(1)

    for i in weight:

        if sum < i:
            return sum + 1
        else:
            sum += i

    return sum + 1