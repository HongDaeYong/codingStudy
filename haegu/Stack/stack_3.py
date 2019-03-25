# [스택, 큐3번]다리- 5번 효율x
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for i in range(bridge_length)]
    while bridge:
        time += 1
        bridge.pop(0)
        if len(truck_weights) > 0 and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        elif len(truck_weights) > 0 and sum(bridge) + truck_weights[0] > weight:
            bridge.append(0)

    return time
