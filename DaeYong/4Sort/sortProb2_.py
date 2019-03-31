"""
한개 틀림
"""


def solution(numbers):
    answer = ''
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)
    for n in numbers:
        answer += str(n)
    return answer


numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]
numbers3 = [3, 33, 300, 330, 333]
print(solution(numbers1))
print(solution(numbers2))
print(solution(numbers3))

