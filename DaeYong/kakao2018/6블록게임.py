import numpy as np


def _check(k, shape, i, j, board):
    for m in range(i):
        for n in range(j, j + shape[1]):
            if k == 0 and n == j:
                continue
            elif k == 1 and n == j + 2:
                continue
            elif k == 2 and n == j:
                continue
            elif k == 3 and n == j + 1:
                continue
            elif k == 4 and n == j + 1:
                continue
            if board[m][n] != 0:
                return False
    return True


def delete_block(shape, i, j, board):
    for m in range(i, i+shape[0]):
        for n in range(j, j+shape[1]):
            board[m][n] = 0
    return board


def may_delete_block(k, board, answer):
    start_idx = 0
    for start_idx, row in enumerate(board):
        if sum(row) != 0:
            break
    if k == 0 or k == 1 or k == 4:
        shape = (2, 3)
    else:
        shape = (3, 2)

    for i in range(start_idx, len(board) - shape[0] + 1):
        for j in range(len(board[0]) - shape[1] + 1):
            if (k == 0 and board[i][j] == board[i+1][j] == board[i+1][j+1] == board[i+1][j+2] != 0 and board[i][j+1] == board[i][j+2] == 0) \
                    or (k == 1 and board[i][j+2] == board[i+1][j] == board[i+1][j+1] == board[i+1][j+2] != 0 and board[i][j] == board[i][j+1] == 0) \
                    or (k == 2 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+2][j+1] != 0 and board[i][j+1] == board[i+1][j+1] == 0) \
                    or (k == 3 and board[i+2][j] == board[i][j+1] == board[i+1][j+1] == board[i+2][j+1] != 0 and board[i][j] == board[i+1][j] == 0) \
                    or (k == 4 and board[i][j+1] == board[i+1][j] == board[i+1][j+1] == board[i+1][j+2] != 0 and board[i][j] == board[i][j+2] == 0):
                if _check(k, shape, i, j, board):
                    board = delete_block(shape, i, j, board)
                    answer += 1
                    return True, board, answer
    return False, board, answer


def solution(board):
    board = np.array(board)
    answer = 0
    block_deleted = True
    while block_deleted:
        block_deleted = False
        for k in range(5):
            isDeleted, board, answer = may_delete_block(k, board, answer)
            if isDeleted:
                block_deleted = True
    return answer


board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
    [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
    [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]
]
print(solution(board))



# # 25점
# import numpy as np
#
# filters = [
#     [[1, 0, 0],
#      [1, 1, 1]],
#     [[0, 1],
#      [0, 1],
#      [1, 1]],
#     [[0, 0, 1],
#      [1, 1, 1]],
#     [[1, 1],
#      [0, 1],
#      [0, 1]],
#     [[0, 1, 0],
#      [1, 1, 1]]
# ]
#
#
# def _check(filter_idx, maskingArea):
#     isBock = False
#     if filter_idx == 0 and maskingArea[0, 0] == maskingArea[1, 0] == maskingArea[1, 1] == maskingArea[1, 2]:
#         isBock = True
#     elif filter_idx == 1 and maskingArea[0, 1] == maskingArea[1, 1] == maskingArea[2, 0] == maskingArea[2, 1]:
#         isBock = True
#     elif filter_idx == 2 and maskingArea[0, 2] == maskingArea[1, 0] == maskingArea[1, 1] == maskingArea[1, 2]:
#         isBock = True
#     elif filter_idx == 3 and maskingArea[0, 0] == maskingArea[0, 1] == maskingArea[1, 1] == maskingArea[2, 1]:
#         isBock = True
#     elif filter_idx == 4 and maskingArea[0, 1] == maskingArea[1, 0] == maskingArea[1, 1] == maskingArea[1, 2]:
#         isBock = True
#     return isBock
#
#
# def findBlock(board, start_idx):
#     for k, ftr in enumerate(filters):
#         ftr = np.array(ftr)
#         for i in range(start_idx, len(board) - len(ftr) + 1):
#             for j in range(len(board[0]) - len(ftr[0]) + 1):
#                 elewise_mul = board[i:i + len(ftr), j:j + len(ftr[0])] * ftr
#                 if 0 < np.sum(elewise_mul) < 1206 and _check(k, elewise_mul):
#                     return True, k, i, j
#     return False, -1, -1, -1
#
#
# def mayEraseBlock(board):
#     start_idx = 0  # 처음으로 0이 아닌 행 번호
#     for start_idx, row in enumerate(board):
#         if sum(row) != 0:
#             break
#     erased, k, i, j = findBlock(board, start_idx)  # filter 에 해당하는 블록 찾기
#     if erased:
#         tmp_mask = np.ones(board.shape, dtype=np.int32)
#         for m in range(len(filters[k])):
#             for n in range(len(filters[k][0])):
#                 tmp_mask[i + m, j + n] -= filters[k][m][n]
#         board *= tmp_mask
#     return erased, board
#
#
# def solution(board):
#     answer = 0
#     board = np.array(board)
#     erased, board = mayEraseBlock(board)
#     while erased:
#         answer += 1
#         erased, board = mayEraseBlock(board)
#     return answer
