import numpy as np

def solution(progresses, speeds):
    answer = []
    pro = np.array(progresses)
    spe = np.array(speeds)
    c = 0
    while c!=len(pro):
        if pro[c] > 100:
            t = 1
            for i in range(c+1,len(pro)):
                if pro[i]<100:
                    break
                t += 1
            c += t
            answer.append(t)
        else:
            pro = pro + spe

    return answer
