def dfs(graph, x, y, visited, func):
    global results
    func += graph[x][y]
    if x == N - 1 and y == N - 1:
        answer = int(func[0])
        op = ''
        for i in range(1, len(func)):
            if i % 2 == 0:
                if op == '+':
                    answer += int(func[i])
                elif op == '*':
                    answer *= int(func[i])
                else:
                    answer -= int(func[i])
            else:
                op = func[i]
        results.append(answer)
        return
    
    if 0 <= x + 1 < N and visited[x+1][y] == 0:
        visited[x+1][y] = 1
        dfs(graph, x+1, y, visited, func)
        visited[x+1][y] = 0
    if 0 <= y + 1 < N and visited[x][y+1] == 0:
        visited[x][y+1] = 1
        dfs(graph, x, y+1, visited, func)
        visited[x][y+1] = 0


N = int(input())
graph = []
for _ in range(N):
    g = list(input().split())
    graph.append(g)

visited = [[0 for _ in range(N)] for _ in range(N)]
visited[0][0] = 1
func = ''
results = []

dfs(graph, 0, 0, visited, '')
print(max(results), min(results))