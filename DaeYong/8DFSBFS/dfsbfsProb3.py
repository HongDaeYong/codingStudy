def drawEdge(node1, node2):
    numDiff = 0
    for s1, s2 in zip(node1, node2):
        if s1 != s2:
            numDiff += 1
    if numDiff == 1:
        return 1
    else:
        return 0


def dfs(grph, vis, i, j):
    vis[i] = 1
    if i == j:
        return 0
    else:
        for k in range(len(vis)):
            if grph[i][k] == 1 and vis[k] == 0:
                return 1 + dfs(grph, vis, k, j)
        return 0


def solution(begin, target, words):
    words.append(begin)
    graph = []
    for w1 in words:
        tmpInternalGraph = []
        for w2 in words:
            tmpInternalGraph.append(drawEdge(w1, w2))
        graph.append(tmpInternalGraph)

    if target not in words:
        return 0

    i = words.index(begin)
    j = words.index(target)
    if graph[i][j] == 1:
        return 1
    else:
        visit = [0 for _ in range(len(words))]
        return dfs(graph, visit, i, j)


inputs = [("hit", "cog", ["hot", "dot", "dog","lot","log","cog"]),
          ("hit", "cog", ["hot", "dot","dog","lot","log"])]
for inpt in inputs:
    print(solution(*inpt))

