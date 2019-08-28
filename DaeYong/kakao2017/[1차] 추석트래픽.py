def decreaseBy(time, amount):
    _time, _amount = time.copy(), amount.copy()
    _time[2] -= _amount[0]
    _time[3] -= _amount[1] - 1
    if _time[3] < 0:
        _time[2] -= 1
        _time[3] += 1000
    if _time[2] < 0:
        _time[1] -= 1
        _time[2] += 60
    if _time[1] < 0:
        _time[0] -= 1
        _time[1] += 60
    return _time


def increaseBy(time, amount):
    _time, _amount = time.copy(), amount.copy()
    _time[2] += _amount[0]
    _time[3] += _amount[1] - 1
    if _time[3] >= 1000:
        _time[2] += 1
        _time[3] -= 1000
    if _time[2] >= 60:
        _time[1] += 1
        _time[2] -= 60
    if _time[1] >= 60:
        _time[0] += 1
        _time[1] -= 60
    return _time


def lower(time1, time2):
    if time1[0] < time2[0]:
        return True
    elif time1[0] > time2[0]:
        return False
    elif time1[1] < time2[1]:
        return True
    elif time1[1] > time2[1]:
        return False
    elif time1[2] < time2[2]:
        return True
    elif time1[2] > time2[2]:
        return False
    elif time1[3] < time2[3]:
        return True
    else:
        return False


def intersect(interval1, interval2):
    if lower(interval1[1], interval2[0]) or lower(interval2[1], interval1[0]):
        return False
    else:
        return True


def solution(lines):
    start_times = []
    end_times = []
    dealing = []
    for line in lines:
        _, e_t, d = line.split()
        e_t = [int(ele) for ele in e_t.replace(':', '.').split('.')]
        end_times.append(e_t)
        d = [int(ele) for ele in d[:-1].split('.')]
        if len(d) == 1:
            d.append(0)
        dealing.append(d)
        s_t = decreaseBy(e_t, d)
        start_times.append(s_t)

    maximum = -1
    for st, et, d in zip(start_times, end_times, dealing):
        cnt = 0
        for _st, _et, _ in zip(start_times, end_times, dealing):
            if intersect([et, increaseBy(et, [1, 0])], [_st, _et]):
                cnt += 1
        if cnt > maximum:
            maximum = cnt
    return maximum


inputs = [
    ["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"],
    ["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"],
    ["2016-09-15 20:59:57.421 0.351s",
     "2016-09-15 20:59:58.233 1.181s",
     "2016-09-15 20:59:58.299 0.8s",
     "2016-09-15 20:59:58.688 1.041s",
     "2016-09-15 20:59:59.591 1.412s",
     "2016-09-15 21:00:00.464 1.466s",
     "2016-09-15 21:00:00.741 1.581s",
     "2016-09-15 21:00:00.748 2.31s",
     "2016-09-15 21:00:00.966 0.381s",
     "2016-09-15 21:00:02.066 2.62s"]
]
for inpt in inputs:
    print(solution(inpt))

