#[완전탐색] 소수찾기

import itertools


def primeNumber(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False

    return True


def solution(numbers):
    answer = 0
    permutate = []
    combinate = []
    for i in range(1, len(numbers) + 1):
        permutate.append(list(map(''.join, itertools.permutations(numbers, i))))

    for i in permutate:
        for j in i:
            combinate.append(int(j))
    combinate = set(combinate)

    for i in combinate:
        if primeNumber(i):
            answer += 1

    return answer