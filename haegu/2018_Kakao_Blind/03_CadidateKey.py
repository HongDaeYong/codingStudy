# 후보키
from itertools import combinations
def solution(relation):
    answer = []
    rows = len(relation)
    cols = len(relation[0])
    colLst = range(cols)
    lst = []
    for leng in range(1, cols + 1):
        comb = combinations(colLst, leng)
        # print("combination ",colLst,", ", leng)
        # print("list(comb) : ", list(comb)) #프린트 하면 다 list(comb) 사라짐
        for i in list(comb):
            tmp = [tuple([item[idx] for idx in i]) for item in relation]
            if len(set(tmp)) == rows:
                # print(set(tmp))
                answer.append(set(i))
    # print(answer)
    for i in answer[:]:
        for j in answer[:]:
            if i == i & j:
                if i != j:
                    answer.remove(j)

    return len(answer)