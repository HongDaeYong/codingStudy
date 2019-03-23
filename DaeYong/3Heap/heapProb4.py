import heapq


def solution(operations):
    minHeap = []
    maxHeap = []
    for op in operations:
        if 'I' in op:
            minHeap.append( int(op[2:]))
            maxHeap.append(-int(op[2:]))
            heapq.heapify(minHeap)
            heapq.heapify(maxHeap)
        elif len(maxHeap) != 0 and op == 'D 1':
            maxPop = heapq.heappop(maxHeap)
            if -maxPop in minHeap:
                minHeap.remove(-maxPop)
        elif len(minHeap) != 0 and op == 'D -1':
            minPop = heapq.heappop(minHeap)
            if -minPop in maxHeap:
                maxHeap.remove(-minPop)

    return1, return2 = 0, 0
    if len(minHeap) != 0:
        return2 = heapq.heappop(minHeap)
    if len(maxHeap) != 0:
        return1 = - heapq.heappop(maxHeap)
    return [return1, return2]

t1 = ['I 16','D 1']
t2 = ['I 7','I 5','I -5','D -1']
t3 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(t1))
print(solution(t2))
print(solution(t3))