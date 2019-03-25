# [스택,큐 4번]기능개발
def solution(progresses, speeds):
    answer = []
    while (len(progresses) > 0):
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while len(progresses) >= 1 and progresses[0] >= 100:
            # print(progresses)
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        if count != 0:
            answer.append(count)

    return answer
