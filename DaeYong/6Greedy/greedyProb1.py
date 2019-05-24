# 33.3점
# def solution(n, lost, reserve):
#     clothes_mask = [1 for _ in range(n)]
#     reserve_mask = {r:1 for r in reserve}
#     for i in range(n):
#         if i+1 in lost:
#             if i+1 in reserve:
#                 reserve_mask[i+1] = 0
#             elif i+2 in reserve and reserve_mask[i+2] != 0:
#                 reserve_mask[i+2] = 0
#             elif i in reserve and reserve_mask[i] != 0:
#                 reserve_mask[i] = 0
#             else:
#                 clothes_mask[i] = 0
#     return sum(clothes_mask)


def solution(n, lost, reserve):
    n2N = [1 for _ in range(n)]
    lost2N = [-1 if i+1 in lost else 0 for i in range(n)]
    reserve2N = [1 if i+1 in reserve else 0 for i in range(n)]

    n2N = [sum(x) for x in zip(n2N, lost2N, reserve2N)]
    for i in range(n-1):
        if n2N[i] + n2N[i+1] == 2:
            n2N[i] = 1
            n2N[i+1] = 1
    n2N = [1 if ele == 2 else ele for ele in n2N]
    return sum(n2N)


inputs = [
    (5, [2, 4], [1, 3, 5]),
    (5, [2, 4], [3]),
    (3, [3], [1]),
    (2, [1], []),
    (5, [1,2,3,4,5], []),
    (10, [1,3,5], [2,7,10])
]
for inpt in inputs:
    print(solution(*inpt))

