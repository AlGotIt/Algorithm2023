# python 3.9

from collections import deque

def solution(maps:list) -> int:
    """
    Args:
        maps (list): 미로 지도

    Returns:
        int: 출구까지의 최단거리
    """
    row = len(maps) # x 
    column = len(maps[0]) # y 

    queue = deque()

    # 이동을 위한 벡터
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 이동 거리 및 방문여부
    visited = [[-1] * column for _ in range(row)]
    visited[0][0] = 1

    queue.append((0, 0))

    # BFS
    while queue:
        # x = 행, y = 열
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어나지 않았을 때
            if 0 <= nx < row and 0 <= ny < column:
                # maps 가 1이고 방문하지 않았거나, 이미 방문했으나 현재 이동거리가 더 적을 경우 
                if maps[nx][ny] and (visited[nx][ny] == -1 or visited[x][y] + 1 < visited[nx][ny]):
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    return visited[-1][-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
