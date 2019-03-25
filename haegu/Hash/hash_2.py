#[해쉬 2번] 전화번호
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book,key=lambda s:len(s))
    index=0
    for i in phone_book:
        for j in phone_book[index+1:]:
            #print(i,j)
            #print(i,j[0:len(i)])
            if i in j and j[0:len(i)]==i:
                return False
        index+=1
    return answer
