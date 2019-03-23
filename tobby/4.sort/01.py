def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        ta = array[i-1:j]
        ta.sort()
        answer.append(ta[k-1])
    
    return answer
