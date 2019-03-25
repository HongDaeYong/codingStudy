def solution(clothes):
    answer = 1
    clothes_map = {}
    for clths in clothes:
        if clths[1] not in clothes_map:
            clothes_map[clths[1]] = 2
        else:
            clothes_map[clths[1]] += 1
    for clths in clothes_map:
        answer *= clothes_map[clths]
    return answer -1


inputs = [
    [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
]
for inpts in inputs:
    print(solution(inpts))

