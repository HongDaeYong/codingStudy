import heapq

def solution(jobs):
    answer = 0
    pq = []
    jobs_sorted = sorted(jobs, key=lambda job: (job[0], job[1]))
    total = 0
    now = 0
    for i in range(len(jobs_sorted)):
        job = jobs_sorted[i]
        heapq.heappush(pq, (now-job[0] + job[1], job)) # priority = wait_time + during_time // (priority, value)
        if i<len(jobs_sorted)-1:
            if jobs_sorted[i+1][0] <= now:
                continue
        job_picked = heapq.heappop(pq)[1]
        total += now - job_picked[0] + job_picked[1]
        now += job_picked[1]
    job_picked = heapq.heappop(pq)[1]
    total += now - job_picked[0] + job_picked[1]
    answer = int(total/len(jobs))
    return answer
