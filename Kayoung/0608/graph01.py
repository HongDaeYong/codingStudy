import queue

def solution(n, edge):
    n += 1
    incidentTable = [[0 for _ in range(n)] for _ in range(n)]
    for e in edge:
        incidentTable[e[0]][e[1]] = 1
        incidentTable[e[1]][e[0]] = 1

    visit = [0 for _ in range(n)]

    curQueue = queue.Queue()
    visit[1] = 1

    for i in range(1, n):
        if incidentTable[1][i] == 1:
            visit[i] = 1
            curQueue.put(i)
    distance = 1

    while(curQueue.qsize() != 0):
        nextQueue = queue.Queue()
        distance += 1
        print(curQueue.queue)
        while(curQueue.qsize() != 0):
            cur = curQueue.get()
            for i in range(1, n):
                if incidentTable[cur][i] == 1 and visit[i] == 0:
                    nextQueue.put(i)
                    visit[i] = 1
        curQueue = nextQueue
    return distance

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))