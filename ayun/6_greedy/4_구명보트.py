def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        boat=[]
        boat.append(people[0])
        boat2=[]
        people.pop(0)
        for i in people:
            if (boat[0]+i)<=limit:
                boat2.append(i)
        if boat2:
            b2=max(boat2)
            boat.append(b2)
            people.remove(b2)
        answer+=1
    return answer