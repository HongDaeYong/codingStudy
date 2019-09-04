def deleteBlock(targetList, board):
    if len(targetList) == 0:
        return 0, board
    deletedCnt = 0
    for target in targetList:
        startX, startY, endX, endY = target[0], target[1], target[0]+1, target[1]+1
        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                if board[i][j] != 0:
                    board[i][j] = 0
                    deletedCnt += 1
    for j in range(len(board[0])):
        zeros = [a for a in range(len(board)) if board[a][j] == 0]
        numZero = len(zeros)
        if numZero == 0:
            continue
        for zeroIdx in zeros:
            board[zeroIdx][j] = board[zeroIdx-numZero][j] if zeroIdx-numZero >= 0 else -1
    return deletedCnt, board


def check(board):
    deleteList = []
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] == -1:
                continue
            if board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                deleteList.append([i, j])
    return deleteList


def solution(m, n, board):
    answer = 0
    board = [[character for character in line] for line in board]
    deleted = -1
    while deleted != 0:
        deleteList = check(board)
        deleted, board = deleteBlock(deleteList, board)
        answer += deleted
    return answer


inputs = [
    (4, 5,
     [
        "CCBDE",
        "AAADE",
        "AAABF",
        "CCBBF"
    ]),
    (6, 6,
     [
        "TTTANT",
        "RRFACC",
        "RRRFCC",
        "TRRRAA",
        "TTMMMF",
        "TMMTTJ"
    ])
]
for inpt in inputs:
    print(solution(*inpt))


# 72.7점
# def deleteBlock(targetList, board):
#     if len(targetList) == 0:
#         return 0, board
#     deletedCnt = 0
#     for target in targetList:
#         startX, startY, endX, endY = target
#         for i in range(startX, endX + 1):
#             for j in range(startY, endY + 1):
#                 if board[i][j] != 0:
#                     board[i][j] = 0
#                     deletedCnt += 1
#     for j in range(len(board[0])):
#         isZero = False
#         zeroIdx = len(board)
#         cnt = 0
#         i = 0
#         for i in range(len(board)-1, 0, -1):
#             if not isZero and board[i][j] == 0:
#                 isZero = True
#                 zeroIdx = i
#             if isZero and board[i][j] == 0:
#                 cnt += 1
#         for i in range(zeroIdx, zeroIdx - cnt, -1):
#             if i-cnt >= 0:
#                 board[i][j] = board[i-cnt][j]
#             else:
#                 board[i][j] = -1
#         if isZero:
#             for k in range(i-1, -1, -1):
#                 if k >= 0:
#                     board[k][j] = -1
#     return deletedCnt, board
#
#
# def check(board):
#     deleteList = []
#     for i in range(len(board)-1):
#         for j in range(len(board[0])-1):
#             if board[i][j] == -1:
#                 continue
#             if board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
#                 deleteList.append([i, j, i+1, j+1])
#     return deleteList
#
#
# def solution(m, n, board):
#     answer = 0
#     board = [[character for character in line] for line in board]
#     deleted = -1
#     while deleted != 0:
#         deleteList = check(board)
#         deleted, board = deleteBlock(deleteList, board)
#         answer += deleted
#     return answer


# 54.5점
# def deleteBlock(targetList, board):
#     if len(targetList) == 0:
#         return 0, board
#     deletedCnt = 0
#     for target in targetList:
#         startX, startY, endX, endY = target
#         for i in range(startX, endX + 1):
#             for j in range(startY, endY + 1):
#                 if board[i][j] != 0:
#                     board[i][j] = 0
#                     deletedCnt += 1
#     for j in range(len(board[0])):
#         isZero = False
#         zeroIdx = len(board)
#         cnt = 0
#         i = 0
#         for i in range(len(board)-1, 0, -1):
#             if not isZero and board[i][j] == 0:
#                 isZero = True
#                 zeroIdx = i
#             if isZero and board[i][j] == 0:
#                 cnt += 1
#         for i in range(zeroIdx, zeroIdx - cnt, -1):
#             if i-cnt >= 0:
#                 board[i][j] = board[i-cnt][j]
#             else:
#                 board[i][j] = -1
#         if isZero:
#             for k in range(i-1, -1, -1):
#                 if k >= 0:
#                     board[k][j] = -1
#     return deletedCnt, board
#
#
# def check(board):
#     deleteList = []
#     for i in range(len(board)-1):
#         for j in range(len(board[0])-1):
#             if board[i][j] == -1:
#                 continue
#             startX, startY, endX, endY = i, j, i, 31
#             for m in range(i+1, len(board)):
#                 if board[i][j] == board[m][j]:
#                     endX = m
#                 else:
#                     break
#             for m in range(i, endX + 1):
#                 tmpEndY = j
#                 for n in range(j, len(board[0])):
#                     if board[i][j] == board[m][n]:
#                         tmpEndY = n
#                     else:
#                         break
#                 if tmpEndY - startY < 1:
#                     endX -= 1
#                     break
#                 elif tmpEndY < endY:
#                     endY = tmpEndY
#             if endY < 31 and endX - startX >= 1 and endY - startY >= 1:
#                 deleteList.append([startX, startY, endX, endY])
#     return deleteList
#
#
# def solution(m, n, board):
#     answer = 0
#     board = [[character for character in line] for line in board]
#     deleted = -1
#     while deleted != 0:
#         deleteList = check(board)
#         deleted, board = deleteBlock(deleteList, board)
#         answer += deleted
#     return answer

