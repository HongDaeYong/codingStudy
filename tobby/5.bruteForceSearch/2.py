import itertools
import math

def solution(numbers):
    
    ns = set()
    for i in range(len(numbers),0,-1):
        ns = ns | set(map(int,map(''.join, itertools.permutations(numbers,i))))
        
    ns = ns - {0,1}
    count = 0

    for n in ns:
        sw = True
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                sw = False
                break
        if(sw):
            count +=1

    return count
