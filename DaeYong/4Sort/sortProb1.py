def solution(array, commands):
    answer = []
    def calculation(arr, comm):
        tmp = arr[comm[0]-1 : comm[1]]
        tmp.sort()
        idx = comm[2] -1
        return tmp[idx]
    for comm in commands:
        answer.append(calculation(array,comm))
    return answer