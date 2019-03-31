import math


def solution(progresses, speeds):
    answer = []
    needs = []
    for p, s in zip(progresses, speeds):
        needs.append(math.ceil(float(100-p)/s))
    print(needs)

    release_day = needs[0]
    release_num = 0
    for need in needs:
        if release_day < need:
            release_day = need
            answer.append(release_num)
            release_num = 1
        else:
            release_num += 1
    answer.append(release_num)
    return answer


progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))

progresses = [45, 70, 56, 80, 10, 24]
speeds = [3, 10, 5, 1, 60, 30]
print(solution(progresses, speeds))