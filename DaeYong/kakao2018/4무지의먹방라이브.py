import numpy as np
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food_times = np.array(food_times)

    def minimum(arr):
        return min(arr, key=lambda x: 100000001 if x == 0 else x)

    def length(arr):
        return sum(arr > 0)

    def leastRounds(food_times, k):
        eat = np.array([-1 if ft != 0 else 0 for ft in food_times])
        numRound, left = divmod(k, length(food_times))
        minRound = min(minimum(food_times), numRound)
        food_times += minRound * eat
        return food_times, (numRound - minRound) * length(food_times) + left

    while k > length(food_times):
        food_times, k = leastRounds(food_times, k)



food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))


# 정확성 만점, 효율성 1개 => 50.0점
# import numpy as np
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     numRound, left = divmod(k, len(food_times))
#
#     eat = np.array([-1 for _ in range(len(food_times))])
#     food_times = np.array(food_times)
#
#     minRound = min(min(food_times), numRound)
#     food_times += minRound * eat
#     food_times = list(food_times)
#
#     food_idx = 0
#     for _ in range((numRound - minRound) * len(food_times) + left):
#         while food_times[food_idx] == 0:
#             food_idx += 1
#             food_idx = 0 if food_idx == len(food_times) else food_idx
#         food_times[food_idx] -= 1
#         food_idx += 1
#         food_idx = 0 if food_idx == len(food_times) else food_idx
#     while food_times[food_idx] == 0:
#         food_idx += 1
#         food_idx = 0 if food_idx == len(food_times) else food_idx
#     return food_idx + 1


# 정확성 만점, 효율성 0점 => 42.9점
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#     food_idx = 0
#     for _ in range(k):
#         while food_times[food_idx] == 0:
#             food_idx += 1
#             food_idx = 0 if food_idx == len(food_times) else food_idx
#         food_times[food_idx] -= 1
#         food_idx += 1
#         food_idx = 0 if food_idx == len(food_times) else food_idx
#     while food_times[food_idx] == 0:
#         food_idx += 1
#         food_idx = 0 if food_idx == len(food_times) else food_idx
#     return food_idx + 1

