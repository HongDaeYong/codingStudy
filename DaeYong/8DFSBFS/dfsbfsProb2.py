def dfs(comp, vis, i):
	vis[i] = 1
	for k in range(len(vis)):
		if k != i and comp[i][k] == 1 and vis[k] == 0:
			dfs(comp, vis, k)

def solution (n, computers):
	answer = 0
	visit = [0 for _ in range(n)]
	for i in range(n):
		if visit[i] == 0:
			dfs(computers, visit, i)
			answer += 1
	return answer