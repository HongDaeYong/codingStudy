answer = 0

def solution(numbers, target):
    global answer
    re(0,target,numbers,0);
    return answer


def re(c, target , numbers, s):
    global answer
    if c == len(numbers):
        if s==target:
            answer += 1
    else :
        re(c+1,target,numbers,s+numbers[c])
        re(c+1,target,numbers,s-numbers[c])