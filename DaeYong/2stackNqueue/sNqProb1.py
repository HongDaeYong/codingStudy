def solution(arrangement):
    answer = 0
    stick = 0
    for i, arr in enumerate(arrangement):
        if arr == '(' and arrangement[i+1] != ')':
            stick += 1
            answer += 1
        elif arr == ')' and arrangement[i-1] != '(':
            stick -= 1
        elif arr == '(' and arrangement[i+1] == ')':
            answer += stick

    return answer


arrangement = "()(((()())(())()))(())"
print(solution(arrangement))
arrangement2 = "(()())"
print(solution(arrangement2))

