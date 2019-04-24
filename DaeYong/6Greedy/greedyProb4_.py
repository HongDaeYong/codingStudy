# 40 점  // 최대 두명만 탈수 있음!! 그 조건 빼먹고 풂.
def solution(people, limit):
    minimum = 40
    rescued = [1 if limit - minimum < person else 0 for person in people]
    answer = sum(rescued)
    while sum(rescued) < len(people):
        boat = 0
        onBoard = {}
        for i, (mask, person) in enumerate(zip(rescued, people)):
            if mask == 1:
                continue
            elif boat + person <= limit:
                rescued[i] = 1
                onBoard[i] = person
                boat += person
            else:
                key_list = list(onBoard.keys())
                key_list.sort(key=lambda x: onBoard[x])
                for j in key_list:
                    if boat < boat - onBoard[j] + person <= limit:
                        rescued[j] = 0
                        boat -= onBoard[j]
                        del onBoard[j]

                        rescued[i] = 1
                        onBoard[i] = person
                        boat += person
                        if boat == limit:
                            break
        answer += 1
    return answer


# 고쳐보는 중
# def solution(people, limit):
#     answer = 0
#     notRescued = {i:person for i, person in enumerate(people)}
#     minimum = 40
#     for i, person in enumerate(people):
#         if len(notRescued) == 0:
#             break
#         elif limit - minimum < person:
#             answer += 1
#             del notRescued[i]
#         elif limit - person in notRescued.values():
#             answer += 1
#             pairIdx = list(notRescued.keys())[list(notRescued.values()).index(limit-person)]
#             if i == pairIdx:
#                 if list(notRescued.values()).count(limit - person) > 1:
#                     pairIdx = list(notRescued.keys())[list(notRescued.values()).index(limit - person, 2)]
#                     del notRescued[i]
#                     del notRescued[pairIdx]
#             else:
#                 del notRescued[i]
#                 del notRescued[pairIdx]
#
#     # left = list(notRescued.values())
#     # left.sort(reverse=True)
#     #
#     # for i in range(len(left)-1):
#     #     for j in range(i+1,len(left)):





inputs = [
    ([70, 50, 80, 50], 100),
    ([70, 80, 50], 100),
    ([100, 50, 40, 70, 90, 40, 40], 120)
]

for inpt in inputs:
    print(solution(*inpt))

