def solution(genres, plays):
    answer = []
    song = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in song:
            song[g] = []
            song[g].append(p)
            song[g].append({p: i})
        else:
            song[g][0] += p
            song[g][1][p] = i
    sortedGenres = sorted(song, key=lambda x:song[x][0], reverse=True)
    for sG in sortedGenres:
        sortedPlays = sorted(song[sG][1], reverse=True)
        for i, sP in enumerate(sortedPlays):
            if i >= 2:
                break
            else:
                answer.append(song[sG][1][sP])
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

