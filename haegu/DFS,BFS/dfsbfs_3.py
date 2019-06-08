# dfs/bfs 단어변환
def change(begin, target, words):
    change_list = []
    for i in words:
        count = 0
        for j in i:
            if j in begin:
                count += 1
        if count == 2:
            change_list.append(i)

    if target in change_list:
        changed = target
        print(change_list, changed)
    else:
        changed = change_list[0]
        words.remove(changed)

        print(change_list, changed)

    return changed


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    for i in range(len(words)):
        begin = change(begin, target, words)
        print(words)
        answer += 1
        if begin == target:
            return answer