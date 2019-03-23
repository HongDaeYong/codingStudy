import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while True:
        if heap[0]>=K:
            break
        if len(heap)==1:
            return -1
        heapq.heappush(heap, heapq.heappop(heap)+(2*heapq.heappop(heap)))
        answer +=1
        
    return answer
