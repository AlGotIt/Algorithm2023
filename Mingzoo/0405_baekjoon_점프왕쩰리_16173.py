# BFS
from collections import deque

# nxn 정사각형 만들기
n = int(input())

# 2차원 배열 정의
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 이동할 두 가지 방향 정의 (아래, 오른쪽)
dx = [1, 0]
dy = [0, 1]

# 방문체크
visited = [[0] * n for _ in range(n)]


def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()

        if graph[x][y] == -1:
            return 'HaruHaru'

        jump = graph[x][y]

        # 점프값을 받아와서 해당값만큼 오른쪽, 아래만 확인
        for i in range(2):
            nx = x + dx[i]*jump
            ny = y + dy[i]*jump

            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            else:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return 'Hing'


# BFS를 수행한 결과 출력
print(bfs(0, 0))
