# [완전탐색] 숫자야구
#ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ
def solution(baseball):
    answer = 0
    for i in range(123, 988):
        check = 0
        a = i // 100
        b = (i % 100) // 10
        c = i % 10
        if a == b or b == c or c == a:
            continue
        elif b == 0 or c == 0:
            continue

        for j in baseball:
            [q, strike, ball] = j
            x = q // 100
            y = (q % 100) // 10
            z = q % 10
            st = 0
            ba = 0
            if a == x:
                st += 1
            if b == y:
                st += 1
            if c == z:
                st += 1
            if a == y or a == z:
                ba += 1
            if b == x or b == z:
                ba += 1
            if c == x or c == y:
                ba += 1
            if [st, ba] == [strike, ball]:
                check += 1
            else:
                break
                # print(i,a,b,c,x,y,z,[st,ba],check)
        if check == len(baseball):
            answer += 1

    return answer