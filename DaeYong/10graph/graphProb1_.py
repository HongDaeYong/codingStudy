import numpy as np


def dfs(grph, vis, i, j):
    vis[i] = 1
    if i == j:
        return 0
    else:
        for k in range(len(vis)):
            if grph[i][k] and vis[k] == 0:
                return 1 + dfs(grph, vis, k, j)
        return 0


def solution(n, edge):
    answer = 0
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for e in edge:
        graph[e[0]-1][e[1]-1] = 1
        graph[e[1]-1][e[0]-1] = 1

    maxDistance = -1
    for node in range(n):
        visit = [0 for _ in range(n)]
        distance = dfs(graph, visit, 0, node)
        if distance > maxDistance:
            maxDistance = distance

    graph = np.array(graph)
    wayGraph = np.ones(graph.shape)
    for _ in range(maxDistance):
        wayGraph = np.matmul(wayGraph, graph)

    for i in wayGraph[0]:
        if i != 0:
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

