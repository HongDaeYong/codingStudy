def solution(n, computers):
    answer = 0
    visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            dfs(i,computers,n,visited)
            answer+=1
    return answer
def dfs(index,computers, n,visited):
    visited[index]=True
    for j in range(n):
        if computers[index][j]==1 and visited[j]==False:
            dfs(j,computers,n,visited)


def solution(n, computers):
    answer = 0
    net=[]
    for i in range(len(computers)):
        for j in range(len(computers)):
            nn=[]
            count=0
            if i<=j:
                if computers[i][j]>=1:
                    for a in net:
                        if i in a or j in a:
                            a.append(j)
                            a.append(i)
                            count+=1
                    if count==0:
                        nn.append(i)
                        nn.append(j)
                        net.append(nn)
    return len(net)
