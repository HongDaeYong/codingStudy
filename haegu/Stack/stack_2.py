#[스택 2번]프린터


def solution(priorities, location):
    answer = 0
    iter = 1
    last = len(priorities)
    while (len(priorities) > 0):
        doc = priorities.pop(0)
        if len(priorities):
            if doc >= max(priorities):
                if location == 0:
                    answer += 1
                    break
                else:
                    location -= 1
                    answer += 1
            else:
                priorities.append(doc)
                if location == 0:
                    location += len(priorities) - 1
                else:
                    location -= 1
        else:
            answer = last

    return answer
