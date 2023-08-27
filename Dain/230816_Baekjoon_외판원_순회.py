def dfs(start, now, value, cnt):
    global mincost
    if cnt == N:
        if costs[now][start]:
            value += costs[now][start]
            if mincost > value:
                mincost = value
        return

    if value > mincost:
        return

    for i in range(N):
        if not visited[i] and costs[now][i]:
            visited[i] = 1
            dfs(start, i, value + costs[now][i], cnt + 1)
            visited[i] = 0


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
mincost = 1000001*16
visited = [0] * N

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(mincost)