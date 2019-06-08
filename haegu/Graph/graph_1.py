def solution(n, edge):
    dist = {}
    answer = 0
    for i in range(2, n + 1):
        dist[i] = 0
    s = []
    for i in edge:
        vertex = i
        if 1 in vertex:
            vertex.remove(1)
            dist[vertex[0]] += 1
            s.append(vertex)
    for i in s:
        edge.remove(i)

    count = 1
    while (count > 0):
        count = 0
        for vertex in edge:
            if dist[vertex[0]] != 0 and dist[vertex[1]] == 0:
                dist[vertex[1]] = dist[vertex[0]] + 1
                count += 1
            elif dist[vertex[1]] != 0 and dist[vertex[0]] == 0:
                dist[vertex[0]] = dist[vertex[1]] + 1
                count += 1
    # print(edge)
    # print(dist)
    a = sorted(dist, reverse=True)
    mx = dist[a[0]]
    answer += 1
    a.pop(0)
    for i in a:
        if mx > dist[i]:
            break
        answer += 1

    return answer