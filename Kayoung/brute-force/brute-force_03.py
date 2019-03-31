def solution(baseball):
    answer = 0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if i==j or j==k or k==i:
                    continue
                isAnswer = True
                for play in baseball:
                    guess = str(play[0])
                    s1 = set([])
                    s1.add(str(i))
                    s1.add(str(j))
                    s1.add(str(k))
                    s2 = set(guess)
                    ball = len(s1 & s2)
                    strike = 0
                    if guess[0] == str(i):
                        strike += 1
                        ball -= 1
                    if guess[1] == str(j):
                        strike += 1
                        ball -= 1
                    if guess[2] == str(k):
                        strike += 1
                        ball -= 1
                    if strike != play[1]:
                        isAnswer = False
                        break
                    if ball != play[2]:
                        isAnswer = False
                        break
                if isAnswer:
                    answer += 1
    return answer

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))