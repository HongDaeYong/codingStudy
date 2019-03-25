class song:
    def __init__(self, genres):
        self.genres = genres
        self.plays = []
        self.total = 0

    def appendSong(self, number, play):
        self.plays.append([number, play])
        self.total += play


def solution(genres, plays):
    answer = []
    songs = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in songs:
            songs[g] = song(g)
        songs[g].appendSong(i, p)

    genresSort = []
    for s in songs:
        songs[s].plays.sort(key=lambda x: x[1], reverse=True)
        genresSort.append([songs[s].genres, songs[s].total])
    genresSort.sort(key=lambda x: x[1], reverse=True)
    print(genresSort)

    for gsort in genresSort:
        answer.append(songs[gsort[0]].plays[0][0])
        answer.append(songs[gsort[0]].plays[1][0])

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

