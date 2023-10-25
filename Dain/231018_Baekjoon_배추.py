"""

2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

5
1
---
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

2
"""

import collections

def earthworm(x,y):
    queue = collections.deque()
    queue.append((x,y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if field[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    
t = int(input()) # tc

for i in range(t):
    n, m, k = map(int, input().split()) # x, y, 배추 개수
    field = [[0] * m for _ in range(n)] # 밭
    visited = [[-1] * m for _ in range(n)] # 방문 저장
    count = 0
    
    for j in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1

    for x in range(n):
        for y in range(m):
            if field[x][y] == 1 and visited[x][y] == -1:
                earthworm(x,y)
                count += 1
    print(count)

