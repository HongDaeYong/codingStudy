# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

import heapq

def solution(scoville, K):
    answer = 0
    pq = []
    if len(scoville) <= 1:
        return -1
    for elem in scoville:
        heapq.heappush(pq, elem)

    while pq[0] < K:
        if len(pq) <= 1:
            return -1
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        sum = a + b * 2
        heapq.heappush(pq, sum)
        answer += 1

    return answer