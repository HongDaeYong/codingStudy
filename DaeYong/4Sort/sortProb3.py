def solution(citations):
    citations.sort()
    for i, paper in enumerate(citations):
        if len(citations) - i <= paper:
            return len(citations) - i
    return 0


citations = [3, 0, 6, 1, 5]
print(solution(citations))

