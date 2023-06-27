N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
white_count = 0
blue_count = 0

def counter(x, y, N):
    global white_count, blue_count
    count = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if board[i][j]:
                count += 1
    if not count:
        white_count += 1
    elif count == N**2:
        blue_count += 1
    else:
        counter(x, y, N // 2)
        counter(x+N // 2, y, N // 2)
        counter(x, y+N //  2, N // 2)
        counter(x+N // 2, y+N //  2, N // 2)
    return

counter(0, 0, N)
print(white_count)
print(blue_count)