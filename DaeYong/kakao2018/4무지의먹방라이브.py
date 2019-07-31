def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    food_idx = 0
    for _ in range(k):
        while food_times[food_idx] == 0:
            food_idx += 1
            food_idx = 0 if food_idx == len(food_times) else food_idx
        food_times[food_idx] -= 1
        food_idx += 1
        food_idx = 0 if food_idx == len(food_times) else food_idx
    while food_times[food_idx] == 0:
        food_idx += 1
        food_idx = 0 if food_idx == len(food_times) else food_idx
    return food_idx + 1


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))

