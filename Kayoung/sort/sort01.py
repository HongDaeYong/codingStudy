# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    for command in commands:
        cut = array[command[0]-1:command[1]]
        cut.sort()
        answer.append(cut[command[2]-1])
    return answer