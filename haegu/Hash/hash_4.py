# [해쉬 4번]베스트앨범
from functools import reduce


def solution(genres, plays):
    answer = []
    id_num = [i for i in range(len(plays))]
    id_arr = []
    song_Info = {}
    song_arr = {}
    genre_Info = {}
    chart = {}
    chart_arr = {}

    for i in zip(plays, id_num):
        song_Info[i[1]] = i[0]
    for i in zip(genres, id_num):
        genre_Info[i[1]] = i[0]
    for k, v in sorted(song_Info.items(), key=lambda song_Info: song_Info[1], reverse=True):
        song_arr[k] = v

    for i in song_arr:
        if genre_Info[i] not in chart:
            chart[genre_Info[i]] = [i]
        else:
            chart[genre_Info[i]].append(i)
    print("chart :", chart)

    for i in chart:
        sum = 0
        for j in chart[i]:
            sum += song_Info[j]
        chart[i].insert(0, sum)

    for k, v in sorted(chart.items(), key=lambda chart: chart[1][0], reverse=True):
        chart_arr[k] = v

    for i in chart_arr:
        if len(chart_arr[i]) <= 2:
            answer.append(chart_arr[i][1])
        else:
            answer.append(chart_arr[i][1])
            answer.append(chart_arr[i][2])

    print("id_num :", id_num)
    print("song_Info :", song_Info)
    print("song_arr :", song_arr)
    print("genre_Info :", genre_Info)
    print("chart :", chart)
    print("chart_arr :", chart_arr)

    return answer
