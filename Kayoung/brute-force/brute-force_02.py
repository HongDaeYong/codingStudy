import itertools

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n is 2:
        return True
    if n % 2 is 0:
        return False
    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i is 0: return False
    return True

def solution(numbers):
    primes = []
    for i in range(1, len(numbers)+1):
        nums = list(map(''.join, itertools.permutations(numbers, i)))
        for num in nums:
            if(is_prime(int(num))):
                primes.append(int(num))
    return len(set(primes))

print(solution("011"))