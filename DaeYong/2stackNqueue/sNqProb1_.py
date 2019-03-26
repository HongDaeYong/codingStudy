class stick:
    def __init__(self):
        self.rasor = 0
        self.isEnd = False

def solution(arrangement):
    answer = 0
    sticks = []
    flushSticks = False
    for i in range(len(arrangement)):
        for s in sticks:
            if not s.isEnd:
                break
            flushSticks = True
        if flushSticks:
            for s in sticks:
                answer += s.rasor + 1
            sticks = []
            flushSticks = False

        if arrangement[i] == '(' and arrangement[i+1] == ')':
            for s in sticks:
                if s.isEnd:
                    break
                else:
                    s.rasor += 1
        elif arrangement[i] == '(' and arrangement[i+1] != ')':
            sticks.append(stick())
        elif arrangement[i] == ')' and arrangement[i-1] != '(':
            for s in reversed(sticks):
                if not s.isEnd:
                    s.isEnd = True
                    break
    return answer


arrangement = "()(((()())(())()))(())"
print(solution(arrangement))
arrangement2 = "(()())"
print(solution(arrangement2))

