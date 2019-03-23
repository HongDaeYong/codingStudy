import heapq
from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min = heappop(scoville)
    while min < K:
        if len(scoville) <= 0:
            return -1
        answer += 1
        heappush(scoville, min + 2 * heappop(scoville))
        min = heappop(scoville)
    return answer