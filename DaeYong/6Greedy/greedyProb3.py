# 90.9 점
# [11 0000000000000 11 ] 이렇게 가운데 A가 왕창 있으면 되돌아가는게 빠름. 이거 틀린듯 // 해결
def solution(name):
    answer = 0
    alphabets = [alpha for alpha in name]
    notWritten = [1 for _ in range(len(name))]

    for i, alpha in enumerate(alphabets):
        if alpha == 'A':
            notWritten[i] = 0
        else:
            answer += min(abs(ord('A') - ord(alpha)), 26 - abs(ord('A') - ord(alpha)))
    maxZeros = -1
    maxZerosEndIdx = 0
    tmpZeros = 0
    for i, nW in enumerate(notWritten):
        if nW == 0:
            tmpZeros += 1
            if maxZeros < tmpZeros:
                maxZeros = tmpZeros
                maxZerosEndIdx = i
        else:
            tmpZeros = 0
    maxZerosStartIdx = maxZerosEndIdx - maxZeros + 1

    if 2 * (maxZerosStartIdx - 1) + (len(name) - maxZerosEndIdx - 1) < maxZeros and maxZerosStartIdx != 0 and maxZerosEndIdx != len(name) - 1:
        return answer + 2 * (maxZerosStartIdx - 1) + (len(name) - maxZerosEndIdx - 1)
    else:
        moveLeft = len(name) - notWritten.index(1) if notWritten[0] != 1 else len(name) - notWritten.index(1, 1)
        notWritten.reverse()
        moveRight = len(name) - notWritten.index(1)
        return answer + min(moveLeft, moveRight)


inputs = [
    # "JEROEN",
    # "JAN",
    "BBAAAAAAAAAAZZ"
]
for inpt in inputs:
    print(solution(inpt))

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

