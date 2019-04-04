def solution(answers):
    answer = []
    count=[]
    onep=[1,2,3,4,5]
    twop=[2,1,2,3,2,4,2,5]
    threep=[3,3,1,1,2,2,4,4,5,5]
    count1=0
    count2=0
    count3=0
    for i in range(0,len(answers)):
        if answers[i]==onep[i%5]:
            count1=count1+1
        if answers[i]==twop[i%8]:
            count2=count2+1
        if answers[i]==threep[i%10]:
            count3=count3+1

    maxcount=max(count1,max(count2,count3))
    if maxcount==count1:
        answer.append(1)
    if maxcount==count2:
        answer.append(2)
    if maxcount==count3:
        answer.append(3)
    return answer