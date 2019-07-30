def solution(record):
    answer = []
    user_name_dict = {}
    for rec in record:
        if len(rec.split()) > 2:
            order, uid, name = rec.split()
            user_name_dict[uid] = name

    in_msg = '님이 들어왔습니다.'
    out_msg = '님이 나갔습니다.'
    for rec in record:
        if len(rec.split()) > 2:
            order, uid, name = rec.split()
        else:
            order, uid = rec.split()

        if order == 'Enter':
            answer.append(user_name_dict[uid] + in_msg)
        elif order == 'Leave':
            answer.append(user_name_dict[uid] + out_msg)
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

