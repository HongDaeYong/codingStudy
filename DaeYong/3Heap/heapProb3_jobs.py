def solution(jobs):
    answer = 0
    for job in jobs:
        answer += job[1]
    previous_end = sum(jobs[0])
    answer += jobs[0][0]

    def returnSec(job):
        return job[1]
    jobs2 = jobs[1:]
    jobs2.sort(key=returnSec, reverse=True)

    for i in range(len(jobs2)):
        answer += abs(previous_end - jobs2[i][0])
        previous_end = abs(previous_end - jobs2[i][0]) + jobs2[i][1]

    return int(answer/len(jobs))

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))