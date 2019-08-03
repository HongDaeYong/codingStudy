def solution(record):
    dic = {} # uid, name
    answer = []

    for r in record:
        l = r.split()
        if(l[0] == "Enter"):
            dic[l[1]] = l[2]
        elif(l[0] == "Leave"):
            continue
        elif(l[0] == "Change"):
            dic[l[1]] = l[2]

    for r in record:
        l = r.split()
        line = dic[l[1]]
        if(l[0] == "Enter"):
            line += "님이 들어왔습니다."
        elif(l[0] == "Leave"):
            line += "님이 나갔습니다."
        elif(l[0] == "Change"):
            continue
        answer.append(line)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))