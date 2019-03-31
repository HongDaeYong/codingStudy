def solution(brown, red):
    answer = []
    for i in range(1, red+1):
        if red % i == 0:
            rw = int(red/i)
            rh = i
            if (rh + rw) * 2 + 4 == brown:
                answer.append(rw+2)
                answer.append(rh+2)
                return answer
    return answer

print(solution(10,2))