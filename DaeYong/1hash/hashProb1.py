def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in enumerate(range(len(completion))):
        if participant[i] != completion[j]:
            return participant[i]
    return participant[-1]


inputs = [(["leo", "kiki", "eden"], ["eden", "kiki"]),
          (["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]),
          (["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])]
for inpts in inputs:
    print(solution(*inpts))

