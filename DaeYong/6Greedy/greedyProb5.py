def solution(routes):
    routes.sort(key=lambda x: x[0])
    answer = 1
    def intersect(r1, r2):
        if r1[1] < r2[0] or r2[1] < r1[0]:
            return -1
        else:
            return [max(r1[0], r2[0]), min(r1[1], r2[1])]
    intersection = routes[0]
    for i in range(1, len(routes)):
        intersection = intersect(intersection, routes[i])
        if intersection == -1:
            answer += 1
            intersection = routes[i]
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))

