#3 탐욕법 큰수 찾기 58.3 속도줄이기
import heapq

def solution(number, k):
    while k > 0:
        compare = []
        for i in range(len(number)):
            num = int(number[:i] + number[i + 1:])
            heapq.heappush(compare, (-num, num))

        number = str(heapq.heappop(compare)[1])

        k -= 1

    return number
