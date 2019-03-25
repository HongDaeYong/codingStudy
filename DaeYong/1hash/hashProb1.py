def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in enumerate(range(len(participant))):
        if participant[i] != completion[j]:
            return participant[i]

inputs = [(["leo", "kiki", "eden"], ["eden", "kiki"]),
          (["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]),
          (["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])]
for inpts in inputs:
    print(solution(*inpts))

