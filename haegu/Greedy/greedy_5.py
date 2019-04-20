#5 탐욕법 섬연결하기 37.5
from operator import itemgetter

def solution(n, costs):
    answer = 0
    d = []
    costs.sort(key=itemgetter(2))
    linked = set([costs[0][0], costs[0][1]])
    answer += costs[0][2]
    costs.pop(0)

    while len(linked) < n:
        d = []
        for j in costs:
            if j[0] in linked or j[1] in linked:
                d.append(j)

        if d == []:
            continue
        else:
            d.sort(key=itemgetter(2))
            linked = linked | set([d[0][0], d[0][1]])
            costs.remove(d[0])
            answer += d[0][2]

    return answer