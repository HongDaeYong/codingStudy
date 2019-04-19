# 힙 - 디스크 컨트롤러

import heapq as hq
from operator import itemgetter


def solution(jobs):
    answer = 0
    throughout = []
    time = 0
    while jobs:
        work_candidate = []
        for i in jobs:
            if time >= i[0]:
                work_candidate.append(i)

        work_candidate.sort(key=itemgetter(1))
        if work_candidate == []:
            time += 1
            continue
        else:
            work_time = work_candidate[0][1]
            time += work_time
            throughout.append(time - work_candidate[0][0])
            jobs.remove(work_candidate[0])

    return sum(throughout) // len(throughout)