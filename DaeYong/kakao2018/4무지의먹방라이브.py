import numpy as np
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    def minimum(arr):
        min = 1000000000
        for a in arr:
            if a != 0 and a < min:
                min = a
        return min
    


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

