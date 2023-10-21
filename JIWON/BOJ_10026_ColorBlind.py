import sys
sys.setrecursionlimit(10000)

def DFS(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return
    if now == grid[y][x] and visited[y][x] == False:
        visited[y][x] = True
        DFS(x+1, y)
        DFS(x-1, y)
        DFS(x, y+1)
        DFS(x, y-1)
        return
    else:
        return
    
N = int(sys.stdin.readline())

grid = []
visited = [[False]*N for i in range(N)]
now = ""
cnt_normal = 0
cnt_colbli = 0

for i in range(N):
    grid.append(list(sys.stdin.readline().strip()))

for j in range(N):
    for i in range(N):
        if not visited[j][i]:
            now = grid[j][i]
            DFS(i,j)
            cnt_normal += 1

for i in range(N):
    for j in range(N):
        visited[j][i] = False
        if grid[j][i] == "G":
            grid[j][i] = "R"

for j in range(N):
    for i in range(N):         
        if not visited[j][i]:
            now = grid[j][i]
            DFS(i,j)
            cnt_colbli += 1

print(cnt_normal, cnt_colbli)