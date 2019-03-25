# [스택/큐 5번]탑
def solution(heights):
    answer = []
    index = 1
    for i in heights:
        receive = heights[:index - 1]
        receive.reverse()
        # print(index,"번째 탑에서 송신,탑 높이: ",i,"수신 탑 높이list :",receive)
        if index == 1:
            answer.append(0)
        else:
            count = index
            for j in receive:
                count -= 1
                # print("count",count)
                if j > i:
                    answer.append(count)
                    break
                elif count == 1:
                    answer.append(0)
                    print(answer)

        index += 1

    return answer
