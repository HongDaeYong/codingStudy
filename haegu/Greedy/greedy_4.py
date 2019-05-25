

def solution(people, limit):
    answer = 0
    people.sort()
    to_be_rescue = len(people)-1
    rescued=0
    while rescued < to_be_rescue:
        if (people[rescued]+people[to_be_rescue]<=limit):
            rescued+=1
            answer+=1
        else:
            answer+=1
        to_be_rescue-=1
    if rescued==to_be_rescue:
        answer+=1


    return answer
