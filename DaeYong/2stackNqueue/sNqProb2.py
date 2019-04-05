import queue


def solution(priorities, location):
    idx = 0
    loc = location
    workQ = queue.Queue()
    for priority in priorities:
        workQ.put(priority)

    while not workQ.empty():
        out = workQ.get()
        popIt = True
        for _ in range(workQ.qsize()):
            tmpOut = workQ.get()
            if out < tmpOut:
                popIt = False
            workQ.put(tmpOut)
        if popIt:
            idx += 1
            if loc == 0:
                return idx
        else:
            if loc == 0:
                loc = workQ.qsize() + 1
            workQ.put(out)
        loc -= 1


priorities1 = [2, 1, 3, 2]
location1 = 2

priorities2 = [1, 1, 9, 1, 1, 1]
location2 = 0

print(solution(priorities1, location1))
print(solution(priorities2, location2))

