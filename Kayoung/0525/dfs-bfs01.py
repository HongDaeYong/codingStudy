cnt = 0


def solution(numbers, target):
    global cnt
    dfs(numbers, 0, target)
    return cnt

def dfs(numbers, cur, target):
    global cnt
    if cur == len(numbers) :
        if sum(numbers) == target:
            cnt += 1
        return

    dfs(numbers, cur + 1, target)
    numbers[cur] *= (-1)
    dfs(numbers, cur + 1, target)

print( solution([1, 1, 1, 1, 1], 3) )
