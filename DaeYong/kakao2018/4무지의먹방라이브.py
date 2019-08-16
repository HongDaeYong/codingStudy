def solution(food_times, k):
    tmp_food_times = food_times.copy()
    tmp_food_times.sort()

    idx, eat, pivot = 0, 0, 0
    for idx in range(len(tmp_food_times)):
        pivot = tmp_food_times[idx]
        eat = tmp_food_times[idx] * len(tmp_food_times) if idx == 0 else \
            (tmp_food_times[idx] - tmp_food_times[idx - 1]) * (len(tmp_food_times) - idx)
        k -= eat
        if k < 0:
            break
    if k > 0 and idx + 1 >= len(tmp_food_times):
        return -1

    answer = 0
    k += eat
    for i in range(idx, len(tmp_food_times)):
        eat = tmp_food_times[idx] if idx == 0 else tmp_food_times[idx] - tmp_food_times[idx - 1]
        k -= eat
        if k < 0:
            break
    k += eat

    while k >= 0:
        if food_times[answer] >= pivot:
            k -= 1
        answer += 1
        answer %= (len(tmp_food_times) - idx)
    return answer + 1


food_times = [3, 1, 2] #  [3,3,3,3,3,3,3] [5,4,2,3,1,5,4] [3, 1, 2]
k = 5 # 15 5
print(solution(food_times, k))


""""""
# 정확성 만점, 효율성 1개 => 50.0점
# def solution(food_times, k):
#     import numpy as np
#     if sum(food_times) <= k:
#         return -1
#     elif len(food_times) > k:
#         return k + 1
#     elif len(food_times) == k:
#         return 1
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

""""""
# 정확성 만점, 효율성 7.1점 => 50.0점
# import numpy as np
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     food_times = np.array(food_times)
#     length = sum(food_times > 0)
#     while k >= length:
#         numRound, left = divmod(k, length)
#         minRound = min(min(food_times, key=lambda x: 100000001 if x == 0 else x), numRound)
#         food_times += np.where(food_times == 0, 0, -minRound)
#         k = (numRound - minRound) * length + left
#         length = sum(food_times > 0)
#     return np.where(np.where(food_times > 0, 1, 0) == 1)[0][k] + 1

""""""
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

