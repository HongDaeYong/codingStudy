# [스택/큐 1번]쇠막대기
def solution(arrangement):
    answer = 0
    stack = []
    for i in range(len(arrangement)):
        if arrangement[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if arrangement[i - 1] == "(":
                answer += len(stack)
            else:
                answer += 1

    return answer
