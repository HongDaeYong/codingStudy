# 실패율 81점
import operator
import heapq
def solution(N, stages):
    answer = []
    dic = {}
    for i in range(1, N + 1):
        a = len(list(filter(lambda x: x >= i, stages)))  # 스테이지에 도달한 플레이어 수
        b = len(list(filter(lambda x: x == i, stages)))  # 스테이지에 도달했지만 아직 클리어하지 못한 수
        if a == 0:
            dic[i] = 0
        else:
            dic[i] = b / a

    answer = heapq.nlargest(len(stages), dic, key=dic.get)  # 81점
    # sorted_dic = sorted(dic.items(), key=operator.i temgetter(1),reverse=True) #81점
    # for i in sorted_dic:
    #     answer.append(i[0])
    return answer