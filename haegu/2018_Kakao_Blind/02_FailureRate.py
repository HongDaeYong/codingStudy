# 실패율 63점
import operator
import heapq
def solution(N, stages):
    answer = []
    dic={}
    for i in range(1,N+1):
        a = len(list(filter(lambda x : x>=i, stages)))
        b = len(list(filter(lambda x : x==i, stages)))
        dic[i]= b/a
    answer = heapq.nlargest(len(stages),dic,key=dic.get)  #63점
    # sorted_dic = sorted(dic.items(), key=operator.i temgetter(1),reverse=True) #63점
    # for i in sorted_dic:
    #     answer.append(i[0])
    return answer