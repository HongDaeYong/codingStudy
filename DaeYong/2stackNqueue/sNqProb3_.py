"""
하나... 시간초과... 왜.... 왜... 왜...!!!
"""


def solution(bridge_length, weight, truck_weights):
    if len(truck_weights) < bridge_length and sum(truck_weights) <= weight:
        return bridge_length + len(truck_weights)
    else:
        weightSum = truck_weights[0]
        bridge = [0 for _ in range(bridge_length-1)] + [truck_weights[0]]
        in_idx = 1
        answer = 1
        while weightSum > 0:
            weightSum -= bridge[0]
            bridge = bridge[1:] + [0]

            if in_idx < len(truck_weights) and weightSum + truck_weights[in_idx] <= weight:
                bridge[-1] = truck_weights[in_idx]
                weightSum += truck_weights[in_idx]
                in_idx += 1
            answer += 1
        return answer


inputs = [
    (2, 10, [7, 4, 5, 6]),
    (100, 100, [10]),
    (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
]
for inpt in inputs:
    print(solution(*inpt))

