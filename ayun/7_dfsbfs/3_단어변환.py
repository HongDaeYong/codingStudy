def solution(begin, target, words):
    answer = 0
    stage = 0
    visited = [False] * len(words)
    for i in range(len(words)):
        if words[i] == target:
            return stage
        if visited[i] == False:
            bfs(i, words[i], target, words, stage, visited)
            print(stage)
    answer = stage
    return answer


def bfs(i, begin, target, words, stage, visited):
    if visited[i] == False and compare(begin, words):
        stage += 1
        visited[i] = True
        print(visited)
        bfs(i, begin, target, words, stage, visited)


def compare(begin, words):
    count = 0
    for j in words:
        ww = set(begin) - set(j)
        if len(ww) == 1:
            count += 1
    if count >= 1:
        return True
    else:
        return False