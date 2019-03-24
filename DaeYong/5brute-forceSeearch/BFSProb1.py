def solution(answers):
    winners = []
    solving = {1:[1,2,3,4,5], 2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5]}
    period = {1:5, 2:8, 3:10}
    scores = {1:0, 2:0, 3:0}
    for i, answer in enumerate(answers):
        for p in period:
            if answer == solving[p][i % period[p]]:
                scores[p] += 1
    max = -1
    for student in scores:
        if scores[student] > max:
            max = scores[student]
    for student in scores:
        if scores[student] >= max:
            winners.append(student)
    winners.sort()
    return winners


answer1 = [1, 2, 3, 4, 5]
answer2 = [1, 3, 2, 4, 2]
print(solution(answer1))
print(solution(answer2))

