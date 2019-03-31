from collections import Counter
def solution(phone_book):
    answer = True
    for i in phone_book:
        num=0
        for j in phone_book:
            if i==j[0:len(i)]:
                num=num+1
        if num>=2:
            return False
    return True