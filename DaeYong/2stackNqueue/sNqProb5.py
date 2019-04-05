def solution(heights):
    answer = []
    for i in reversed(range(len(heights))):
        received = False
        for j in reversed(range(len(heights[:i]))):
            if heights[j] > heights[i]:
                received = True
                answer.append(j+1)
                break
        if not received:
            answer.append(0)
    return list(reversed(answer))


inputs = [[6, 9, 5, 7, 4], [3, 9, 9, 3, 5, 7, 2], [1, 5, 3, 6, 7, 6, 5]]
for inpt in inputs:
    print(solution(inpt))

