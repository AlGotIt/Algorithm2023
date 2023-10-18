import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
arr = [
    list(input())
    for _ in range(n)
]
visited = [
    [0]*n
    for _ in range(n)
]

dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]
cnt = 0


def in_range(x, y):
    if (x < 0 or y < 0 or x >= n or y >= n or visited[x][y] == 1):
        return False
    return True


def dfs(x, y):
    global cnt
    # if x == n-1 and y == n-1:
    #     print(cnt, end=" ")
    #     return
    visited[x][y] = 1
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        if in_range(new_x, new_y):
            if arr[new_x][new_y] == arr[x][y]:
                dfs(new_x, new_y)


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1
print(cnt, end=" ")

for i in range(n):
    for j in range(n):
        if (arr[i][j] == 'G'):
            arr[i][j] = 'R'

visited = [
    [0]*n
    for _ in range(n)
]

cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1
print(cnt)
