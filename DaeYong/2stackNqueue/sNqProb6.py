def solution(prices):
    answer = []
    for i in range(len(prices)):
        fallen = False
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                fallen = True
                break
        if not fallen:
            answer.append(len(prices[i+1:]))
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))

