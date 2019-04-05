#[완전탐색] 모의고사
def solution(answers):
    answer = []
    su_1 = [1, 2, 3, 4, 5]
    su_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one = 0
    two = 0
    three = 0
    for i in range(len(answers)):
        if answers[i] == su_1[i % len(su_1)]:
            one += 1
        if answers[i] == su_2[i % len(su_2)]:
            two += 1
        if answers[i] == su_3[i % len(su_3)]:
            three += 1
    score = {1: one, 2: two, 3: three}
    sorted(score)
    for i in score:
        if answer == []:
            answer.append(i)
        else:
            if score[i] == score[answer[0]]:
                answer.append(i)

    answer.sort()
    return answer