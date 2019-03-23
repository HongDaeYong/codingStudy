
import heapq as hq
def solution(operations):
    answer = []
    for i in operations:
        if i[0] == 'I':
            answer.append(int(i[1:]))
        else:
            if answer == []:
                continue
            elif int(i[1:]) == -1:
                answer.remove(min(answer))
            else:
                answer.remove(max(answer))
    if answer == []:
        return [0, 0]
    else:
        return [max(answer), min(answer)]
