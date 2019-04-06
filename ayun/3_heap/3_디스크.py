import numpy
def solution(jobs):
    answer = []
    time=[]
    start=[]
    for i in jobs:
        start.append(i[0])
    # jobs.sort(key=lambda st:st[0])
    time.append(jobs[0][1]-jobs[0][0])
    ini=jobs.pop(0)
    while jobs:
        jobs2=[]
        for j in range(len(jobs)):
            if jobs[0][1]>jobs[j][0]:
                jobs2.append(jobs[j])
        jobs2.sort(key=lambda st:st[1])
        for k in range(len(jobs2)):
            time.append((time[len(time)-1]+jobs2[k][1]))
            jobs.remove(jobs2[k])
    start2=zip(start,time)
    start3=[]
    for i in start2:
        start3.append(i[1]-i[0])
    return numpy.mean(start3)