def solution(answers):
    answer = []
    a = []
    a.append([1,2,3,4,5])
    a.append([2,1,2,3,2,4,2,5])
    a.append([3,3,1,1,2,2,4,4,5,5])
    point = [0,0,0]
    
    max_count = 0
    for i in range(len(a)):
        k = 0
        for j in answers:
            if a[i][k] == j:
                point[i] += 1
            k = (k+1)%len(a[i])
    
    max_point = max(point)
    for i in range(len(a)):
        if max_point == point[i]:
            answer.append(i+1)
        
    return answer
