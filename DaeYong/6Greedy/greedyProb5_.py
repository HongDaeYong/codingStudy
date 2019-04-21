# def solution(n, costs):
#     answer = 0
#     connected = []
#     costs.sort(key=lambda x: x[2])
#     for cost in costs:
#         if cost[0] not in connected or cost[1] not in connected:
#             answer += cost[2]
#             if cost[0] not in connected:
#                 connected.append(cost[0])
#             if cost[1] not in connected:
#                 connected.append(cost[1])
#     return answer


# 프림 알고리즘 사용
def solution(n, costs):
    answer = 0
    connected = [0]
    for i in range(n-1):
        pass

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

