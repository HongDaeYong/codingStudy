# dfs/bfs 여행경로
def find_flight(tickets, start, answer):
    flight = []
    for i in range(len(tickets)):
        if start == tickets[i][0]:
            flight.append(tickets[i])

    flight.sort()
    print(flight)
    tickets.remove(flight[0])
    start = flight[0][1]
    answer.append(start)
    return start


def solution(tickets):
    answer = []
    answer.append("ICN")
    start = answer[-1]
    while (tickets):
        start = find_flight(tickets, start, answer)

    return answer