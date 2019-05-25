cnt = 0


def solution(numbers, target):
    global cnt
    dfs(numbers, 0, target)
    return cnt

def sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

def dfs(numbers, cur, target):
    global cnt
    if cur == len(numbers):
        return

    dfs(numbers, cur + 1, target)
    if sum(numbers) == target:
        cnt += 1
        return

    numbers[cur] *= -1
    dfs(numbers, cur + 1, target)
    if sum(numbers) == target:
        cnt += 1
        return



print( solution([1, 1, 1, 1, 1], 3) )
