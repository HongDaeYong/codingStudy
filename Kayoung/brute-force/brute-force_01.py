# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3


person1 = [1, 2, 3, 4, 5]  # 5
person2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10

def solution(answers):
    answer = []
    cnt = {1: 0, 2: 0, 3: 0}
    for i in range(len(answers)):
        if answers[i] == person1[i%5]:
            cnt[1] += 1
        if answers[i] == person2[i%8]:
            cnt[2] += 1
        if answers[i] == person3[i%10]:
            cnt[3] += 1
    answer = [name for name, count in cnt.items() if count == max(cnt.values())]
    return answer

print(solution([1,3,2,4,2]))