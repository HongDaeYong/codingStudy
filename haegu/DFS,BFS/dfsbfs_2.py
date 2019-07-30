# dfs/bfs 네트워크
def linked(i, n, computers, link):
    link[i] = 1
    for j in range(n):
        if (link[j] == 0 and computers[i][j] == 1):
            linked(j, n, computers, link)


def solution(n, computers):
    answer = 0
    link = [0 for i in range(n)]
    for i in range(n):
        if link[i] == 0:
            linked(i, n, computers, link)
            answer += 1
        if 0 not in link:
            break

    return answer