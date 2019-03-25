#[스택/큐 6번]-효율x
def solution(prices):
    answer=[]
    while len(prices):
        a = prices.pop(0)
        count = 0
        for i in prices:
            if a<=i:
                count+=1
            else:
                count+=1
                break
        answer.append(count)
    return answer
