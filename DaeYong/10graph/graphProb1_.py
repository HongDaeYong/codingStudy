class node:
    def __init__(self, nodeNum):
        self.num = nodeNum
        self.connected = []
        self.distFrom1 = 0 if nodeNum == 1 else -1

    def connect(self, edge):
        if edge[0] == self.num:
            self.connected.append(edge[1])
        elif edge[1] == self.num:
            self.connected.append(edge[0])


def solution(n, edge):
    answer = 0
    graph = [node(i+1) for i in range(n)]
    for e in edge:
        for nd in graph:
            nd.connect(e)

    

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

