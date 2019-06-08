import queue

def solution(begin, target, words):
    mapLen = len(words) + 1
    changableMap = makeChangableMap(begin, words)

    visit = []
    for i in range(mapLen):
        visit.append(0)

    curQueue = queue.Queue()
    visit[mapLen-1] = 1
    if target not in words:
        return 0

    for i in range(mapLen):
        if changableMap[mapLen-1][i] == 1:
            visit[i] = 1
            curQueue.put(i)
            if words[i] == target: #words를 안 거치고 변환가능한 경우
                return 1
    distance = 1

    while(curQueue.qsize() != 0):
        nextQueue = queue.Queue()
        while(curQueue.qsize() != 0):
            cur = curQueue.get()
            print("cur : ", cur)
            for i in range(mapLen):
                if changableMap[cur][i] == 1 and visit[i] == 0:
                    if words[i] == target:
                        return distance
                    nextQueue.put(i)
                    visit[i] = 1
        distance += 1
        curQueue = nextQueue
    return 0


def makeChangableMap(begin, words):
    mapLen = len(words) + 1
    changableMap = [[0 for _ in range(mapLen)] for _ in range(mapLen)]  # words + begin + target

    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            if isChangable(words[i], words[j]):
                changableMap[i][j] = 1
                changableMap[j][i] = 1

    for i in range(len(words)):
        if isChangable(words[i], begin):
            changableMap[mapLen - 1][i] = 1
            changableMap[i][mapLen - 1] = 1

    return changableMap

def isChangable(str1, str2):
    if str1 == str2:
        return False
    if len(str1) != len(str2):
        return False
    cnt = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            cnt += 1
    if cnt == len(str1) - 1:
        return True
    return False


print(solution("hit", "dog", ["hot", "dot", "dog", "lot", "log", "cog"]))