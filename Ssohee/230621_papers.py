# 백준 1780 종이의 개수
# https://www.acmicpc.net/problem/1780

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
zero, minus, one = 0, 0, 0

def dfs(x, y, n):
    global zero, minus, one
    start = li[x][y]    #해당 사분면의 (0,0) 원소

    for i in range(x, x+n):
        for j in range(y, y+n):
            if li[i][j] != start:
                dfs(x, y, n//3) #1번
                dfs(x, y + n//3, n//3)  #2번
                dfs(x, y + n//3 * 2, n//3)  #3번
                dfs(x + n//3, y, n//3)  #4번
                dfs(x + n // 3, y + n // 3, n // 3) #5번
                dfs(x + n // 3, y + n // 3 * 2, n // 3) #6번
                dfs(x + n // 3 * 2, y, n // 3)  #7번
                dfs(x + n // 3 * 2, y + n // 3, n // 3) #8번
                dfs(x + n // 3 * 2, y + n // 3 * 2, n // 3) #9번
                return

    if start == -1: minus += 1
    elif start == 0: zero += 1
    elif start == 1: one += 1

dfs(0, 0, n)
print(minus, zero, one)
