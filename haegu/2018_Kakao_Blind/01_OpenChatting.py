# 오픈채팅방
def solution(record):
    answer = []
    enter = "님이 들어왔습니다."
    out = "님이 나갔습니다."
    dic={}
    for i in record:
        if i.split()[0]!="Leave":
            dic[i.split()[1]]=i.split()[2]
    for i in record:
        r = i.split()
        if r[0]=="Enter":
            answer.append(dic[r[1]]+enter)
        elif r[0]=="Leave":
            answer.append(dic[r[1]]+out)
    return answer