def solution(genres, plays):
    answer = []
    twoLVhash = {}
    for id, (gen, pl) in enumerate(zip(genres, plays)):
        if gen not in twoLVhash:
            twoLVhash[gen] = {}
        twoLVhash[gen][id] = pl

    srtd = sorted(twoLVhash.items(), key=lambda x: sum(x[1].values()), reverse=True)
    for sd in srtd:
        tmpSd = sorted(sd[1].items(), key=lambda x: x[1], reverse=True)
        answer.append(tmpSd[0][0])
        if len(tmpSd) > 1:
            answer.append(tmpSd[1][0])
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

