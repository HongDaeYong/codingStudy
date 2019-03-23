import heapq

def solution(operations):
    answer = []
    q = []
    
    for op in operations :
        opArray = op.split(' ')
        if opArray[0] =='I':
            heapq.heappush(q,int(opArray[1]))
        else :
            if len(q)==0 :
                continue
            if opArray[1]=='-1':
                heapq.heappop(q)
            else:
                q.pop(q.index(max(q)))
                       
    if len(q)==0 :
        return [0,0]
    
    return [max(q),min(q)]
