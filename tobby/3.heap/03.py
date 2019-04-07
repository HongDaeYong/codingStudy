import heapq

def solution(jobs):
    answer = 0
    waitQ = []
    jobs.sort(key=lambda job : (job[0],job[1]))

    now = 0
    i = 0
    c = 0
    while(c != len(jobs)):
        for j in range(i, len(jobs)):
            if jobs[i][0] <= now :
                heapq.heappush(waitQ,(jobs[i][1],jobs[i][0]))
                if i < len(jobs):
                    i+=1
        if(len(waitQ)==0):
            now = jobs[i][0]
            continue
        todo = heapq.heappop(waitQ)
        answer += now - todo[1] + todo[0]
        now = now + todo[0]
        c+=1
    return answer // len(jobs)
