# 8.3점
# def solution(number, k):
#     lenNumber = len(number)
#     number_mask = [1 for _ in range(lenNumber)]
#
#     i = 0
#     while sum(number_mask) > lenNumber - k:
#         if number_mask[i % lenNumber] == 0:
#             i += 1
#             continue
#         offset = 1
#         while i % lenNumber + offset < lenNumber and number_mask[i % lenNumber + offset] == 0:
#             offset += 1
#         if i % lenNumber != lenNumber - 1 and number[i % lenNumber] < number[i % lenNumber + offset]:
#             number_mask[i % lenNumber] = 0
#         i += 1
#
#     answer = ''
#     for i, num in enumerate(number):
#         if number_mask[i]:
#             answer += num
#     return answer


# 83.3 점
# def solution(number, k):  # 시간 엄청 줄여야함. 개빠른 진모형 코드도 시간초과남;;
#     def one(num):
#         for i in range(len(num)-1):
#             if num[i] < num[i+1]:
#                 return num.replace(num[i], '', 1)
#     for _ in range(k):
#         number = one(number)
#     return number[:-(len(number))]


# 찾은 정답 ;;; 개쩖;;;
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


inputs = [
    ("1924", 2),
    ("1231234", 3),
    ("4177252841", 4)
]
for inpt in inputs:
    print(solution(*inpt))

