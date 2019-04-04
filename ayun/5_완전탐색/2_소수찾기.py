import itertools
def solution(numbers):
    answer = 0
    new=[]
    for i in range(1,len(numbers)+1):
        for perm in itertools.permutations(numbers,i):
            new.append(int("".join(perm)))
    for i in set(new):
        for j in range(2,i+1):
            if i==j:
                answer=answer+1
            if i%j ==0:
                break
    return answer