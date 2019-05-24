def solution(people, limit):
    people.sort()
    print(people)
    big = len(people) - 1
    count = 0
    small=0
    while(small<=big):
        if people[small]+people[big] <= limit :
            small +=1
        count += 1
        big -=1
    return count