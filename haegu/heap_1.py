
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    mix_1 = heapq.heappop(heap)
    while mix_1 < K:
        answer += 1
        if len(heap) >= 1:
            mix_2 = heapq.heappop(heap)
            heapq.heappush(heap, mix_1 + mix_2 * 2)
        else:
            return -1
            break
        mix_1 = heapq.heappop(heap)

    return answer