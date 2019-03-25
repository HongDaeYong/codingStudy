
import heapq as hq
def solution(citations):
    answer=0
    citations.sort()
    num=len(citations)
    if citations[0]>=num:
        return num
    for i in range(num):
        if hq.nlargest(num-i,citations,lambda s:s>=num-i)[-1]>=num-i:
            return num-i
    return 0