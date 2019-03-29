import queue


def solution(bridge_length, weight, truck_weights):
    if len(truck_weights) < bridge_length and sum(truck_weights) <= weight:
        return bridge_length + len(truck_weights)
    elif
    answer = 1
    idx = 1
    bridge = queue.Queue()
    bridge.maxsize = bridge_length
    weightSum = truck_weights[0]
    bridge.put([truck_weights[0], bridge_length])
    while not bridge.empty():
        for _ in range(bridge.qsize()):
            out = bridge.get()
            out[1] -= 1
            if out[1] == 0:
                weightSum -= out[0]
            else:
                bridge.put(out)
        if idx < len(truck_weights):
            if weightSum + truck_weights[idx] < weight:
                weightSum += truck_weights[idx]
                bridge.put([truck_weights[idx], bridge_length])
                idx += 1
        answer += 1
    return answer


inputs = [(2, 10, [7, 4, 5, 6]), (100, 100, [10]), (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])]
for inpt in inputs:
    print(solution(*inpt))

