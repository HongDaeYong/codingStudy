#2 탐욕법 조이스틱 63.6점
def solution(name):
    answer = 0
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    name_dict = {}
    location = []
    for i, n in enumerate(name):
        if n == 'A':
            continue
        else:
            name_dict[i] = n
            location.append(i)

    print(name_dict)
    for i in name_dict:
        if name_dict[i] < 'N':
            answer += alphabet.index(name_dict[i])
        else:
            answer += len(alphabet) - alphabet.index(name_dict[i])

    if len(location) == len(name):
        return answer + len(name) - 1
    else:
        cursur = 0
        for i in location:
            if i - cursur > len(name) / 2:
                location.reverse()
                print(cursur, i, len(name) - i - cursur)
                answer += len(name) - i - cursur
                cursur = i

            else:
                print(cursur, i, i - cursur)
                answer += i - cursur
                cursur = i

        print(location)
        return answer
