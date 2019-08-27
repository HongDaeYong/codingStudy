def increaseBy(time, amount):
    h, m = divmod(amount, 60)
    hour = int(time[:2]) + h
    minute = int(time[3:]) + m
    if minute >= 60:
        hour += 1
        minute -= 60
    return '{0:02d}'.format(hour) + ':' + '{0:02d}'.format(minute)


def decreaseBy(time, amount):
    h, m = divmod(amount, 60)
    hour = int(time[:2]) - h
    minute = int(time[3:]) - m
    if minute < 0:
        hour -= 1
        minute += 60
    return '{0:02d}'.format(hour) + ':' + '{0:02d}'.format(minute)


def solution(n, t, m, timetable):
    timetable.sort()
    departures = [increaseBy("09:00", i*t) for i in range(n)]
    boarded = [0 for _ in range(n)]
    departure_time = ['' for _ in timetable]
    for i, crew in enumerate(timetable):
        for j, departure in enumerate(departures):
            if boarded[j] >= m:
                continue
            elif crew <= departure:
                boarded[j] += 1
                departure_time[i] = departure
                break

    if boarded[-1] < m:
        return departures[-1]
    else:
        try:
            idx = departure_time.index('') - 1
        except ValueError:
            idx = len(timetable) - 1
        return departure_time[idx] if boarded[-1] < m else decreaseBy(timetable[idx], 1)


inputs = [
    (1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]),
    (2, 10, 2, ["09:10", "09:09", "08:00"]),
    (2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]),
    (1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]),
    (1, 1, 1, ["23:59"]),
    (10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
]

for i, inpt in enumerate(inputs):
    print(i, solution(*inpt))

