import numpy as np
def solution(citations):
    c = np.array(citations)
    for h in range(max(c)):
        if h <= np.sum(c>=h):
            return h
