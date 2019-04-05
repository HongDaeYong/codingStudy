# [완전탐색] 카펫
##ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ
def solution(brown, red):
    answer = []
    width = brown + red
    for i in range(1, width + 1):
        if width % i == 0:
            a = width // i
            b = i
            # print(a,b)
            if a > 2 and b > 2 and ((a - 2) * (b - 2)) == red:
                return [a, b]
