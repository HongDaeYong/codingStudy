def solution(weight):
    weight.sort()
    print(weight)
    s = 1
    for i in weight:
        if s < i:
            break
        s += i
    return s

print(solution([3, 1, 6, 2, 7, 30, 1]))