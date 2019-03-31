def solution(priorities, location):
    answer=0
    while True:
        p=priorities.pop(0)
        l=len(priorities)
        if p>=max(priorities):
            answer=answer+1
            if location==0:
                return answer
            location=location-1
        else:
            priorities.append(p)
            location=location-1
            if location<0:
                location=location+l+1