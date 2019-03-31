from collections import Counter
def solution(participant, completion):
    count=Counter(participant)
    count2=Counter(completion)
    for i in participant:
        if count[i]!=count2[i]:
            return i