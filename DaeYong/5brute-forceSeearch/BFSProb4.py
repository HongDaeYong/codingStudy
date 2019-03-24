def isRightSize(brown, red, width, height):
    if width < height:
        return False
    elif brown == 2 * width + 2 * height - 4 and red == (width - 2) * (height - 2):
        return True
    return False


def solution(brown, red):
    for i in range(1, 2499 + 1): # maximum width = (5000-2)/2 = 2499
        for j in range(1, 1414 + 1): # maximum height = sqrt(2000000) = 1414
            if isRightSize(brown, red, i, j):
                return [i, j]


browns = [10,  8, 24]
reds   = [ 2,  1, 24]
for b,r in zip(browns, reds):
    print(solution(b, r))

